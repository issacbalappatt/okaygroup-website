import Lenis from 'lenis';
import 'lenis/dist/lenis.css';
import { animate } from 'motion/mini';

const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
const pointer = window.matchMedia('(any-pointer: fine)');
const easing = [0.22, 1, 0.36, 1];
const activeAnimations = new Set();
let scrolling;

function play(element, keyframes, options) {
  const animation = animate(element, keyframes, { ease: easing, ...options });
  activeAnimations.add(animation);
  animation.then(() => activeAnimations.delete(animation));
}

function updateScrolling() {
  scrolling?.destroy();
  scrolling = undefined;
  if (preference.matches) {
    for (const animation of activeAnimations) animation.cancel();
    activeAnimations.clear();
    return;
  }

  if (pointer.matches) {
    scrolling = new Lenis({ autoRaf: true, lerp: 0.16, stopInertiaOnNavigate: true });
  }
}

preference.addEventListener('change', updateScrolling);
pointer.addEventListener('change', updateScrolling);
updateScrolling();

const hero = document.querySelector('.hero');
if (hero && !preference.matches && !location.hash && window.scrollY < 50) {
  play(hero.querySelector('picture'), { transform: ['scale(1.045)', 'scale(1)'] }, { duration: 1.65 });
  for (const [index, element] of [...hero.querySelector('.hero-copy').children].entries()) {
    play(element, { opacity: [0.3, 1], transform: ['translateY(14px)', 'translateY(0)'] },
      { duration: 0.75, delay: index * 0.075 });
  }
}

const observer = new IntersectionObserver((entries) => {
  for (const { target, isIntersecting } of entries) {
    if (!isIntersecting) continue;
    observer.unobserve(target);
    if (!preference.matches && !target.matches(':focus-within')) {
      play(target, { opacity: [0.55, 1], transform: ['translateY(14px)', 'translateY(0)'] }, { duration: 0.65 });
    }
  }
}, { threshold: 0.16 });

for (const element of document.querySelectorAll('.split-title, .tile, .about-preview .about-grid, .callout .wrap')) {
  observer.observe(element);
}

document.addEventListener('okay:catalogue-change', (event) => {
  if (preference.matches) return;
  for (const [index, card] of [...event.target.children].entries()) {
    play(card, { opacity: [0.4, 1], transform: ['translateY(8px)', 'translateY(0)'] },
      { duration: 0.45, delay: index * 0.035 });
  }
});
