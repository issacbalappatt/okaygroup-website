# Okay Group website

Public website for Okay Group and Manorama Oxygen in Kalamassery, Kerala. This is a static site. Serve the repository root with `python3 -m http.server 8000` to preview it. GitHub Pages deploys pushes and merges to `main`. The `CNAME` file sets the production domain.

## Editing the catalogue and coverage

Edit the buying copy in `scripts/catalogue_content.py` and the shared templates in `scripts/build_site.py`. Run `python3 scripts/build_site.py` and commit the generated HTML and sitemap with the source changes. The sitemap contains all canonical public pages and is advertised in `robots.txt`.

Okay Group confirmed it operates branches across Kerala and offers delivery across the state. The coverage page lists delivery districts and the confirmed corporate office. Customers can enquire about the specific branch serving their address.

## Site animation

Install the pinned dependencies with `npm ci` and run `npm run build` when editing `src/motion.js`. Commit the regenerated `assets/motion.js` and `assets/motion.css` so GitHub Pages can serve them with the rest of the static site. [Motion](https://github.com/motiondivision/motion) handles entrances and catalogue transitions. [Lenis](https://github.com/darkroomengineering/lenis) eases mouse-wheel scrolling. Both respect the visitor’s reduced-motion preference. Touch scrolling stays native.

## Research and editorial notes

Reviewed on 19 November 2026. Historical records establish the business history and past activity. Current stock, delivery and operating permits should be confirmed directly with the business.

### Group and companies

| Entity | Evidence |
| --- | --- |
| Okay Group | The September 2020 KSIDC profile dates the original Kalamassery oxygen plant to 1996 and describes its original role supplying medical oxygen in Kerala. It records past expansion into oxygen at Thiruvananthapuram, Kollam, Kottayam, Kozhikode and Palakkad, acetylene at Kalamassery and carbon dioxide at Udyogamandal, Kollam and Kozhikode. The Justdial date of 2016 differs from the KSIDC account and the 1996 Manorama Oxygen incorporation record. |
| Manorama Oxygen Private Limited | Registered in Ernakulam on 19 August 1996, CIN U24111KL1996PTC010661 and GSTIN 32AABCM6073D1ZV. The company’s Indeed profile explicitly identifies it as part of Okay Group. Its IndiaMART profile and local industrial association listing support the product and Kalamassery location information. |
| Manorama Carbonic Pvt. Ltd. | Incorporated 4 March 1985, CIN U31908KL1985PTC004154. The corporate record lists overlapping directors and the Okay Group email. A 2016 KSPCB order identifies its Udyogamandal facility and a validity date in 2018. This is historical evidence. |
| Roopresmi Private Limited | Incorporated in 1995, CIN U28113KL1995PTC009634. Corporate records show overlapping directorships. A 2021 PESO directory lists an oxygen site in Manvila and the same email as Manorama Oxygen. The historical listing gives a September 2021 expiry. |
| Ajay Oxygen Private Limited | Incorporated 15 February 2011, CIN U24111KL2011PTC027679. Corporate records show the same registered address as Manorama Oxygen and overlapping directorships. A distinct current plant or product range could not be verified. |

The public website describes Manorama Oxygen as a group company and the other three as associated companies. Share ownership, formal subsidiary status and the full roster of group companies require confirmation from the group.

### Product evidence

- Manorama Oxygen’s IndiaMART catalogue lists medical oxygen, oxygen cylinders and Dura cylinders, portable oxygen equipment, carbon dioxide gas and liquid carbon dioxide, gaseous and liquid nitrogen, cryocans and tanks, commercial and high-purity argon, liquid argon, helium cylinders and dry ice blocks.
- KDPIA lists industrial oxygen, medical oxygen and gaseous nitrogen. The 2020 KSIDC profile records acetylene production at Kalamassery. The website directs acetylene enquiries to the team for current availability.
- FACT’s July 2019 purchase order register records an argon order placed with Manorama Oxygen. This corroborates historical supply and is not used as a current customer endorsement or product purity guarantee.
- Kerala Government Order 386/2022/ID records a proposed liquid medical oxygen public-private partnership involving Manorama Oxygen and a separate proposal from Ozone Gases. No commissioning was verified. The order does not establish an ownership link with Ozone Gases.
- The group email is published by KDPIA and appears in corporate records. The site uses the public Kalamassery office address. Postal codes differ across historical sources. The current IndiaMART area listing, Justdial and a public tender award place the organisation in Kalamassery. The tender lists 683104.

### Sources

1. [KSIDC Investor Konnect, September 2020, Okay Group profile](https://www.kbip.org/uploads/newsletter/12021-04-08-065243.pdf)
2. [Manorama Oxygen IndiaMART company profile](https://www.indiamart.com/manorama-oxygen-pvtltd/profile.html) and [product catalogue](https://www.indiamart.com/manorama-oxygen-pvtltd/products-and-services.html)
3. [Kalamassery Development Plot Industries Association member listing](https://kdpia.com/members08.html)
4. [Manorama Oxygen company description on Indeed](https://in.indeed.com/cmp/Manorama-Oxygen-Pvt-Ltd-1)
5. [Manorama Oxygen corporate record](https://www.zaubacorp.com/MANORAMA-OXYGEN-PRIVATE-LIMITED-U24111KL1996PTC010661), [Manorama Carbonic corporate record](https://www.tofler.in/manorama-carbonic-pvt-ltd/company/U31908KL1985PTC004154), [Roopresmi corporate record](https://www.zaubacorp.com/ROOPRESMI-PRIVATE-LIMITED-U28113KL1995PTC009634), [Ajay Oxygen corporate record](https://www.zaubacorp.com/AJAY-OXYGEN-PRIVATE-LIMITED-U24111KL2011PTC027679)
6. [PESO oxygen filling and storage licence directory, May 2021](https://peso.gov.in/web/sites/default/files/2021-06/GCR%20Form%20EF%209-May-2021_0.pdf)
7. [Kerala State Pollution Control Board historical consent renewal for Manorama Carbonic](https://ocmms.nic.in/OCMMS_NEW/download.action?applicationId=1046662&industryFor=air&industryState=Kerala&industryType=CTO)
8. [Kerala Government Order 386/2022/ID](https://document.kerala.gov.in/documents/governmentorders/govtorder1105202216%3A38%3A26.pdf)
9. [FACT July 2019 purchase order register](https://fact.co.in/images/upload/PO-DETAILS-JULY-2019_22.10.2019_492_303.pdf)
10. [Government Medical College Ernakulam medical gas tender award listing](https://tenderkart.in/tender/dac2c6dc-df2f-4922-8b0f-e7da6d17f1e6)
11. [Okay Group corporate office on Justdial](https://www.justdial.com/Ernakulam/Okay-Group-Of-Companies-Corporate-Office-Major-Industrial-Estate-Kalamassery/0484PX484-X484-160627211512-X2G5_BZDET)

The catalogue structure, supply formats and application navigation draw on [INOX Air Products](https://inoxairproducts.com/what-we-do/). The products are based on the Okay Group and Manorama Oxygen sources above. The specialty gas form accepts sourcing enquiries, including nitrous oxide, which appears in a [public trade listing](https://www.indianyellowpages.com/ernakulam/manorama-oxygen-pvt-ltd-kalamassery-ernakulam-4230992/). Confirm current availability directly.

The studio cylinder hero, warehouse and product artwork are illustrative.
