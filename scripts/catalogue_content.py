"""Buyer-facing copy for the gas catalogue, application pages and guides."""

PRODUCT_DETAILS = {
    'industrial-oxygen': (
        'Industrial Oxygen Cylinder Supply in Kerala',
        'Enquire about industrial oxygen cylinders from Okay Group for oxy-fuel cutting, fabrication and other industrial uses, with delivery across Kerala.',
        [
            ('Oxygen for metalworking', 'Industrial oxygen supports combustion in processes such as oxy-fuel cutting. Metal shops should identify the process, existing cylinder arrangement and expected usage when ordering. This helps the supplier confirm compatibility and determine how often the shop needs replenishment.'),
            ('What to include in an oxygen enquiry', 'Send the oxygen grade or specification on your purchase order, the cylinder size or valve connection your equipment requires, and the number of cylinders you need. If your facility already holds cylinders, mention whether you need an exchange or a new supply arrangement.'),
            ('Industrial and medical grades', 'Keep the application on the order. Healthcare buyers should use the medical oxygen enquiry and provide their facility’s purchasing and documentation requirements.'),
        ],
        ('acetylene', 'argon', 'medical-oxygen'),
    ),
    'nitrogen': (
        'Nitrogen Gas & Liquid Nitrogen Supply in Kerala',
        'Enquire about nitrogen cylinders and cryogenic liquid nitrogen in Kerala. Share your required purity, form, usage and delivery location.',
        [
            ('Gaseous nitrogen', 'Nitrogen is used in applications such as purging, inerting and blanketing. For cylinder enquiries, include your required purity, application and approximate monthly usage. Instrument buyers should supply the specification from their equipment documentation, including any impurity limits.'),
            ('Liquid nitrogen', 'Liquid nitrogen is used for cryogenic cooling and some freezing applications. Tell us the amount per fill, refill frequency and what container your site uses. If you also need a cryocan or storage tank, make that part of the same enquiry.'),
            ('How to specify the order', 'Identify whether you require gas or liquid and use the same unit for the quantity and expected consumption. Include the site postcode and your requested first delivery.'),
        ],
        ('liquid-nitrogen-equipment', 'argon', 'helium'),
    ),
    'argon': (
        'Argon Gas Cylinder & Liquid Argon Enquiries in Kerala',
        'Ask about commercial argon, high-purity argon and liquid argon for fabrication, welding and analytical work across Kerala.',
        [
            ('Argon for fabrication', 'Argon is a shielding gas used in welding. The gas requirement can differ by welding process and material, so cite the gas or mixture on your welding procedure when you enquire. Include your cylinder format and how many cylinders the shop uses in a typical week.'),
            ('Argon for instrument use', 'Laboratories and instrumentation teams may need a grade specified by their equipment manufacturer. Include the instrument make and model, minimum purity and any listed impurity limits. Commercial and high-purity argon are separate purchasing specifications.'),
            ('Cylinder or liquid supply', 'State the form you need and whether the order is a one-off or recurring requirement. For liquid enquiries, also give the expected volume and existing on-site storage details.'),
        ],
        ('carbon-dioxide', 'helium', 'nitrogen'),
    ),
    'carbon-dioxide': (
        'Carbon Dioxide Gas & Liquid CO₂ in Kerala',
        'Enquire about gaseous and liquid carbon dioxide in Kerala for fabrication, beverage carbonation or other applications. Include the grade your process requires.',
        [
            ('Specify your CO₂ application', 'Carbon dioxide can be used for carbonation and in some welding applications. Beverage buyers should state their food-contact grade and documentation requirements. Fabrication buyers should state whether their procedure calls for carbon dioxide or a specific gas mixture.'),
            ('Choose the form for your equipment', 'Give the required form, the cylinder or vessel connection your equipment uses, and the typical volume per order. For recurring supply, share your usual consumption and any seasonal changes that affect it.'),
            ('Solid carbon dioxide', 'For shipping or temperature-controlled packing, ask about dry ice blocks. Order those by the required weight and dispatch date so the team can confirm the appropriate supply arrangements.'),
        ],
        ('dry-ice', 'argon', 'nitrogen'),
    ),
    'acetylene': (
        'Dissolved Acetylene Cylinder Enquiries in Kerala',
        'Ask Okay Group about dissolved acetylene cylinder availability and delivery for oxy-fuel cutting and fabrication in Kerala.',
        [
            ('Acetylene for fabrication', 'Dissolved acetylene is a fuel gas used in oxy-fuel fabrication. Buyers should specify their process, cylinder connection and the number of cylinders required. If you also need industrial oxygen, include it on a separate line so the two orders can be quoted clearly.'),
            ('Cylinder availability', 'Specify whether you need a fresh supply or a cylinder exchange and where the cylinders will be delivered. For scheduled jobs, share the start date and whether the site has restrictions on delivery hours or access.'),
            ('Purchasing documentation', 'Tell the team which product documents your site requires. Your equipment supplier or site safety team can verify the appropriate installation and handling requirements for your setup.'),
        ],
        ('industrial-oxygen', 'argon', 'carbon-dioxide'),
    ),
    'helium': (
        'Helium Gas Cylinder Enquiries in Kerala',
        'Enquire about helium cylinders for leak detection or analytical work in Kerala. Include your required grade, pressure and cylinder connection.',
        [
            ('Helium for instrument use', 'Helium can be used for analytical instruments and some leak-detection systems. The instrument or testing specification should identify the required purity. Include a copy or the exact grade and impurity limits in your enquiry so the team can check what can be sourced.'),
            ('Details to put on the request', 'Provide the cylinder size or connection, required quantity and intended delivery date. Include your expected consumption if you need recurring supply. If the gas is part of a blend, write the complete mixture specification.'),
            ('Grade and availability', 'Let us know whether your purchasing team needs a specification sheet or analysis documentation. Ask the team to confirm availability and lead time for the requested grade.'),
        ],
        ('argon', 'nitrogen'),
    ),
    'medical-oxygen': (
        'Medical Oxygen Cylinder Supply for Healthcare in Kerala',
        'Request medical oxygen supply for a hospital or healthcare facility in Kerala. Include your cylinder requirements, delivery location and purchasing documentation.',
        [
            ('Supply for healthcare procurement', 'For a healthcare supply enquiry, give the facility name, delivery address and procurement contact. Specify the oxygen format called for in your purchase request, the quantity needed per delivery and the expected frequency. State whether you are adding a supply point or replacing an existing arrangement.'),
            ('Cylinder and Dura cylinder enquiries', 'Tell us which format your facility has specified and any site-specific receiving arrangements. If you are comparing formats, share the existing installation details and ask what is available for that site.'),
            ('Documentation for your facility', 'Include the documents your procurement or compliance team requires before ordering. For equipment enquiries, browse the separate oxygen equipment page.'),
        ],
        ('oxygen-equipment',),
    ),
    'oxygen-equipment': (
        'Oxygen Cylinder Kits & Concentrator Enquiries in Kerala',
        'Enquire about portable oxygen cylinder kits and concentrators listed by Manorama Oxygen. Ask about current models, availability and documentation in Kerala.',
        [
            ('Portable cylinder kits', 'If your enquiry is for a portable kit, identify the cylinder arrangement and the accessories required by your purchase specification. Tell us whether you need the complete kit, a particular component or a replacement for an existing unit.'),
            ('Concentrator enquiries', 'Share any make, model or performance requirements already specified by your facility. Include the intended site, number of units and any requirements for manuals, warranty information or supplier documentation.'),
            ('Oxygen supply and equipment', 'A recurring medical oxygen supply request and an equipment purchase are different enquiries. Include any ongoing cylinder refill needs alongside the equipment enquiry so the team can identify what needs to be quoted.'),
        ],
        ('medical-oxygen',),
    ),
    'liquid-nitrogen-equipment': (
        'Liquid Nitrogen Cryocans & Storage Tank Enquiries in Kerala',
        'Ask about cryocans or liquid nitrogen storage tanks. Share your capacity, vessel type, application and location in Kerala.',
        [
            ('Cryocans and tanks', 'Identify whether you need a portable cryocan or a larger storage vessel. Include the required capacity, intended application and whether there is an existing container on site. If replacing a vessel, a model reference or specification helps the team identify what to check.'),
            ('Plan for refills', 'Share expected consumption, refill frequency and where the vessel will be received or filled. A container request and an ongoing liquid nitrogen supply request can be discussed together.'),
            ('Documents to request', 'Ask for the vessel specification and any supporting documentation your facility needs before purchase. The responsible site team should confirm compatibility with its storage and receiving arrangements.'),
        ],
        ('nitrogen', 'dry-ice'),
    ),
    'dry-ice': (
        'Dry Ice Blocks and Delivery Enquiries in Kerala',
        'Ask about dry ice blocks in Kerala for temperature-controlled transport. Include the weight, dispatch date, postcode and collection or delivery preference.',
        [
            ('Dry ice for cold-chain packing', 'Dry ice is solid carbon dioxide. It may be specified for temperature-controlled shipments or other cooling applications. Ask about blocks and provide the required weight for each dispatch. If your packing process calls for particular block dimensions, include them in your request.'),
            ('Book around dispatch', 'Dry ice sublimates into carbon dioxide gas. Coordinate the collection or delivery window with your packing schedule and have your logistics team confirm the packaging and transport requirements.'),
            ('Repeat orders', 'If you ship regularly, provide the expected order frequency, typical volume and any seasonal peaks. State if you are packing at more than one site so the delivery team can check arrangements for each location.'),
        ],
        ('carbon-dioxide', 'nitrogen'),
    ),
}

APPLICATION_DETAILS = {
    'fabrication': (
        'Industrial Gases for Manufacturing and Metal Fabrication',
        'Plan gas supply for manufacturing and metal fabrication in Kerala, including industrial oxygen, nitrogen, argon and dissolved acetylene.',
        [
            ('Cutting, welding and process requirements', 'Start with each workstation or process. Oxy-fuel cutting, welding and gas purging have different specifications. Use the gas named on the process documentation and flag cylinder connections or purity requirements that differ across the site.'),
            ('Estimate replenishment', 'Collect consumption figures by workshop or shift. Average use helps establish a recurring order and peak use helps the team discuss stock for large fabrication jobs. Identify shutdown or project dates when a larger order may be needed.'),
            ('Prepare one purchasing list', 'Send a separate line for each gas and grade. Put your delivery postcode, receiving contact and access requirements on the same request.'),
        ],
        ('industrial-oxygen', 'acetylene', 'argon', 'nitrogen'),
    ),
    'healthcare': (
        'Medical Oxygen Supply for Hospitals and Healthcare Facilities',
        'Request healthcare oxygen supply and equipment in Kerala. Include your facility’s oxygen format, usage, delivery schedule and documentation.',
        [
            ('Confirm the facility specification', 'Send the procurement requirement for medical oxygen, including the cylinder or liquid format specified for your site, expected usage and supporting documents. If managing supply for several facilities, list the volumes and locations separately.'),
            ('Discuss receiving arrangements', 'Share the contact responsible for inventory, any delivery windows and whether the enquiry is for the first delivery or replenishment. The team can then discuss order arrangements and product availability.'),
            ('Equipment requests', 'Specify the equipment model or requirements separately from the gas order. Include any manuals, compliance documents or warranty information your procurement team needs.'),
        ],
        ('medical-oxygen', 'oxygen-equipment'),
    ),
    'laboratories': (
        'Laboratory, Analytical and Research Gas Enquiries',
        'Enquire about laboratory gases in Kerala, including nitrogen, argon and helium. Share instrument specifications, purity and cylinder format.',
        [
            ('Start with the instrument documentation', 'Copy the gas specification used by the instrument or procedure, including purity and maximum impurity levels if stated. For an instrument installation, the make and model and connection requirements help identify the appropriate enquiry.'),
            ('Identify the grade for each use', 'An analytical instrument, an inerting step and a cooling process may need different grades or forms. Keep them on separate lines in the request. Include your anticipated usage when you need regular replenishment.'),
            ('Cryogenic requirements', 'For liquid nitrogen, provide the volume per fill and any container requirements. If the laboratory needs a cryocan, include its required capacity in the enquiry.'),
        ],
        ('nitrogen', 'argon', 'helium', 'liquid-nitrogen-equipment'),
    ),
    'food': (
        'Gas Enquiries for Food and Beverage Producers',
        'Discuss carbon dioxide and nitrogen enquiries for food and beverage applications such as carbonation and cooling, with Kerala delivery.',
        [
            ('Carbonation and processing', 'A beverage producer enquiring about carbon dioxide should state the food-contact grade and documentation requested by its quality team. List the product form, expected consumption and delivery schedule.'),
            ('Nitrogen for cooling enquiries', 'Tell us whether the process calls for gaseous or liquid nitrogen. For cryogenic liquid, include the quantity per fill and any existing storage vessel. If one facility orders more than one form or grade, identify each explicitly.'),
            ('Seasonal and recurring volumes', 'Include production peaks, planned line changes and any separate receiving locations. If ordering for cold-chain dispatch, include the date and quantity of dry ice required on a separate line.'),
        ],
        ('carbon-dioxide', 'nitrogen', 'dry-ice'),
    ),
    'welding': (
        'Welding and Cutting Gas Enquiries in Kerala',
        'Ask about argon, carbon dioxide, industrial oxygen and dissolved acetylene for fabrication shops across Kerala.',
        [
            ('Shielding gas', 'Shielding gas depends on the welding process and material. Read the gas specified by the welding procedure or equipment supplier and tell us whether you need a pure gas or a mixture. Include the mixture composition if the procedure specifies one.'),
            ('Oxy-fuel cutting', 'For an oxy-fuel enquiry, identify the oxygen and fuel gas requirements separately. List the cylinder sizes and valve connections called for by the equipment documentation and the quantity for each gas.'),
            ('Workshop or project orders', 'Send the number of workstations, usual usage and expected start date. Tell us if the order is for delivery to a temporary fabrication site and who will receive it.'),
        ],
        ('argon', 'carbon-dioxide', 'industrial-oxygen', 'acetylene'),
    ),
    'cold-chain': (
        'Dry Ice and Gas Enquiries for Cold-Chain Logistics',
        'Plan dry ice block orders for temperature-controlled shipments in Kerala. Share your dispatch schedule, volume and delivery location.',
        [
            ('Work back from the dispatch window', 'Tell us when and where your shipment will be packed and the weight of dry ice required. Confirm with your logistics team what packaging and transport conditions the shipment requires.'),
            ('Single and recurring shipments', 'Provide order quantities per dispatch, the number of shipments per week and any peak weeks. If packing at more than one location, list the requirement and receiving contact for each site.'),
            ('Separate cooling requirements', 'If your operation uses liquid nitrogen for a facility process as well as dry ice for shipping, list those as separate orders. They have different supply and receiving arrangements.'),
        ],
        ('dry-ice', 'nitrogen', 'carbon-dioxide'),
    ),
}

SUPPLY_DETAILS = {
    'cylinder-supply': (
        'Gas Cylinder Supply and Delivery in Kerala',
        'Enquire about packaged industrial and medical gas cylinders, exchange arrangements and recurring delivery across Kerala.',
        [
            ('Identify the cylinder on the purchase request', 'Give the gas and grade, cylinder capacity or size, and the connection or valve on your equipment. Share the quantity needed and state whether this is a first order, replenishment or an exchange enquiry.'),
            ('Plan reorders around consumption', 'For regular supply, indicate typical usage and your busy periods. If your site holds several grades of the same gas, list them separately. Make room on the order for any required product or delivery paperwork.'),
            ('Give receiving details', 'Include your postcode, site access restrictions and preferred receiving hours. Ask the team to confirm product availability and the delivery or collection arrangement for your site.'),
        ],
        ('industrial-oxygen', 'nitrogen', 'argon'), 'general', 'industrial-cylinders',
    ),
    'bulk-liquid': (
        'Bulk and Cryogenic Liquid Gas Supply Enquiries',
        'Discuss liquid nitrogen, liquid argon and liquid carbon dioxide enquiries for sites in Kerala. Include consumption and receiving arrangements.',
        [
            ('Describe the site and liquid requirement', 'State the gas requested, expected volume and required frequency. If there is already storage or receiving equipment at the site, share its capacity and any supplier requirements documented by the site team.'),
            ('Compare one-off and regular supply', 'A one-off order needs a usable delivery window and clear receiving information. A recurring requirement also needs normal and peak usage estimates, so the team can discuss an arrangement that suits the site.'),
            ('Provide a contact for technical details', 'Include the name of the person responsible for the receiving installation. For cryocans or liquid nitrogen tanks, include the vessel requirement alongside the liquid enquiry.'),
        ],
        ('nitrogen', 'argon', 'carbon-dioxide', 'liquid-nitrogen-equipment'), 'bulk-liquid', 'gas-facility',
    ),
    'dry-ice-supply': (
        'Dry Ice Ordering, Collection and Delivery',
        'Find out what to include in a dry ice block order for collection or delivery in Kerala, from required weight to dispatch date.',
        [
            ('Set the order weight and timing', 'Give the total weight, preferred block size if specified, and when the material will be used. Confirm whether you want to collect it or need a delivery to the packing site.'),
            ('Prepare for repeat deliveries', 'List volumes by day or week and note any slow periods or shipment peaks. If you have several dispatch points, provide a delivery postcode and receiving contact for each.'),
            ('Check logistics with your receiving team', 'Ask your logistics team what paperwork, packaging and handling requirements apply. Tell us if there are delivery access restrictions or a specific receiving window.'),
        ],
        ('dry-ice', 'carbon-dioxide'), 'dry-ice', 'dry-ice',
    ),
    'product-documentation': (
        'Request Gas Specifications and Safety Data Sheets',
        'Request gas specifications, safety data sheets and other purchasing documentation for industrial and medical gas enquiries.',
        [
            ('Identify the specific product', 'Give the gas name, grade, physical form and reference number if you have it. For a mixture, include the composition on your purchase specification. These details help the team identify the documentation for the product you intend to order.'),
            ('State which documents you need', 'Specify whether you are asking for a safety data sheet, a product specification or other documentation requested by your site. If you have a procurement checklist, include its document names or required standards.'),
            ('Request documents before the order if needed', 'Tell us whether the request is for a quote, supplier onboarding or an existing order. If it relates to an existing order, include the purchase order or delivery reference.'),
        ],
        ('industrial-oxygen', 'medical-oxygen'), 'documentation', 'gas-facility',
    ),
}

GUIDES = {
    'request-a-gas-quote': (
        'How to Request an Industrial Gas Quote',
        'A purchasing checklist for industrial gas enquiries, including grade, cylinder size, quantity, delivery postcode and documentation.',
        [
            ('Write one line for each product', 'Use the product name, grade, form and quantity. For example, the requested details for a nitrogen cylinder purchase include the grade, cylinder size and number of cylinders. Use your process or instrument documentation to fill in the specification.'),
            ('Add the site and schedule', 'Provide the delivery postcode, desired first delivery date and how frequently you expect to order. For an existing arrangement, note whether you use an exchange or own the cylinders. For recurring orders, give a typical and a peak volume.'),
            ('Include any supporting paperwork', 'List what your procurement team needs with the quote. For several sites, give each site a separate line with its quantity and location.'),
        ],
        ('supply/cylinder-supply.html', 'supply/product-documentation.html', 'locations.html'),
    ),
    'cylinders-vs-bulk': (
        'Gas Cylinders vs Bulk Liquid Supply',
        'Compare the information needed to price packaged cylinders and bulk liquid gas supply for your site in Kerala.',
        [
            ('When asking about cylinders', 'Identify how many workstations or receiving points use the gas, the cylinder size and how often the cylinders are replaced. A count of full and empty cylinders over a typical period helps your team estimate how much to order.'),
            ('When asking about liquid supply', 'Share the gas and liquid volume, existing tank or vessel details and access for delivery. Include peak usage and tell us whether the requirement is a single fill or recurring supply.'),
            ('What to compare', 'Ask for an itemised quote and use the same time period for both estimates. Check delivery frequency, any cylinder or equipment terms and the receiving space your site can support.'),
        ],
        ('supply/cylinder-supply.html', 'supply/bulk-liquid.html', 'gases/nitrogen.html'),
    ),
    'gas-grade-and-purity': (
        'How to Specify Gas Grade and Purity',
        'Learn what to include when ordering an industrial, laboratory or medical gas grade, from purity to required product documentation.',
        [
            ('Use the application specification', 'Copy the required gas grade from the equipment manual, welding procedure or purchasing specification. If it gives both a minimum purity and maximum amounts for specific impurities, include both. For a blend, list each component and tolerance if specified.'),
            ('Keep application and grade together', 'A gas name alone may be insufficient for purchasing. A production process, laboratory instrument and healthcare facility can each call for a different specification or documentation even if they use the same gas name.'),
            ('State the supply format', 'Add whether you need a cylinder, liquid supply or a solid product. Include quantity and the documentation your facility needs before deciding on a supplier.'),
        ],
        ('supply/product-documentation.html', 'applications/laboratories.html', 'gases/argon.html'),
    ),
    'planning-recurring-delivery': (
        'Planning Recurring Gas Deliveries Across Kerala',
        'Plan recurring gas orders by postcode, consumption, receiving windows and peak usage. A checklist for multi-site buyers in Kerala.',
        [
            ('Build a simple order record', 'For each site, record the gas, grade, typical volume and usual order frequency. If your purchasing team orders for several facilities, keep the delivery locations and receiving contacts with the site-level quantities.'),
            ('Plan around peaks', 'Flag shutdown maintenance, project starts or seasonal output that can change consumption. If delivery is limited to particular times, make those windows part of the enquiry.'),
            ('Agree on receiving details', 'Ask which branch serves the location, when the expected delivery can be arranged and which documents will accompany it. Provide updated receiving information when work moves to a different site.'),
        ],
        ('locations.html', 'supply/cylinder-supply.html', 'supply/bulk-liquid.html'),
    ),
}

DISTRICTS = (
    'Thiruvananthapuram', 'Kollam', 'Pathanamthitta', 'Alappuzha',
    'Kottayam', 'Idukki', 'Ernakulam', 'Thrissur', 'Palakkad', 'Malappuram',
    'Kozhikode', 'Wayanad', 'Kannur', 'Kasaragod',
)
