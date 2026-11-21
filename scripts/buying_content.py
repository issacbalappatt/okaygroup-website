"""Detailed format and application pages for recurring purchasing enquiries."""

BUYING_PAGES = {
    'oxygen-cylinders': (
        'Oxygen Cylinders in Kerala for Industry and Healthcare',
        'Find the right Okay Group enquiry for industrial or medical oxygen cylinders. Include your cylinder format, quantity and delivery PIN code.',
        'general', 'industrial-cylinders', ('industrial-oxygen', 'medical-oxygen'),
        [
            ('Choose the right procurement route', 'If the order is for metal cutting or fabrication, use the industrial oxygen specification from your process documents. If the order is for a healthcare facility, use the medical oxygen specification and identify the documents your procurement team requires.'),
            ('Check what your facility calls the cylinder', 'Share the cylinder size or model reference, required connection and the number of cylinders. A description such as “large cylinder” can mean different things across sites. Refer to your existing approved specification if possible.'),
            ('Order, refill or exchange', 'Say whether you are setting up a new supply, enquiring about an exchange, or adding stock for a particular job. For recurring orders, give your estimated consumption and delivery town, district and PIN code.'),
        ],
    ),
    'liquid-nitrogen': (
        'Liquid Nitrogen Supply Enquiries in Kerala',
        'Request liquid nitrogen for cryogenic cooling, laboratory or process applications. Include the volume per fill, vessel and delivery location.',
        'nitrogen', 'gas-facility', ('nitrogen', 'liquid-nitrogen-equipment'),
        [
            ('Define the volume per fill', 'Give the intended amount of liquid nitrogen and state the unit used in your purchase request. If this is for several vessels, list the capacity and requested fill amount for each vessel, along with the approximate refill interval.'),
            ('Tell us what is already on site', 'Identify whether you have a cryocan or a larger tank. Provide the approved receiving specification, where the vessel is located and the site contact handling receipt. If you also need a vessel, include that in the enquiry.'),
            ('Schedule the delivery', 'Share the Kerala delivery address, PIN code and preferred date or recurring window. For a laboratory or food-processing order, include the grade or documentation your team has specified.'),
        ],
    ),
    'nitrogen-cylinders': (
        'Nitrogen Gas Cylinder Enquiries in Kerala',
        'Ask about gaseous nitrogen cylinders for purging, blanketing, fabrication or instrument use. Share your purity and cylinder requirements.',
        'nitrogen', 'cylinder-nitrogen', ('nitrogen', 'liquid-nitrogen-equipment'),
        [
            ('Match grade to the job', 'Identify whether the gaseous nitrogen is used for a plant process, a workshop operation or an instrument. Include the grade in the procedure and any stated limits for moisture or other impurities. For instrument use, attach or reference the gas specification.'),
            ('State your cylinder configuration', 'Include the cylinder size, valve connection, quantity and any site requirements for an exchange. If a manifold or other site equipment is already in use, use its approved gas and cylinder specification in your request.'),
            ('Estimate cylinder usage', 'Give the number of cylinders used in a normal week and during peak use. For an occasional job, state the quantity, site location and date the cylinders are needed.'),
        ],
    ),
    'carbon-dioxide-cylinders': (
        'CO₂ Cylinder Supply Enquiries in Kerala',
        'Ask about carbon dioxide cylinders for fabrication, carbonation or other specified uses. Include the grade, cylinder size, quantity and delivery PIN code.',
        'carbon-dioxide', 'cylinder-co2', ('carbon-dioxide', 'dry-ice'),
        [
            ('Specify the use and grade', 'Write whether the gas is for beverage carbonation, a welding process or another application. Refer to your existing purchase specification. If procurement requires food-contact documentation, list those documents with the enquiry.'),
            ('Describe your cylinder order', 'Use the cylinder size or fill weight and connection shown on your existing specification. Give the number of cylinders and indicate any exchange arrangements you already have. For a new installation, send the cylinder requirements provided by your equipment supplier.'),
            ('Order CO₂ separately from mixtures and dry ice', 'If your welding procedure calls for a mixture, include its exact composition as a separate item. A dry ice order should list block weight and dispatch timing rather than cylinder information.'),
        ],
    ),
    'liquid-carbon-dioxide': (
        'Liquid Carbon Dioxide Supply Enquiries in Kerala',
        'Enquire about liquid CO₂ for recurring industrial or beverage requirements in Kerala. Share your grade, volumes and storage details.',
        'carbon-dioxide', 'gas-facility', ('carbon-dioxide', 'dry-ice'),
        [
            ('Give your expected volume', 'Provide the amount of liquid CO₂ per delivery and how often the facility expects to order. If your use varies with production output, include typical and peak requirements so the supplier can discuss the delivery arrangement.'),
            ('Include site receiving information', 'Tell us whether there is an existing vessel and share the required receiving specification with the location and site contact. List any dates when the installation is expected to be commissioned or ready to receive supply.'),
            ('Confirm the grade you need', 'Give the grade on the purchase specification and identify any documents required by your production or quality team. If you are comparing liquid and cylinder supply, note both in the enquiry.'),
        ],
    ),
    'medical-oxygen-dura-cylinders': (
        'Medical Oxygen Dura Cylinder Enquiries in Kerala',
        'Request information on medical oxygen Dura cylinder options for healthcare facilities. Include your facility specification and delivery schedule.',
        'medical-oxygen', 'medical', ('medical-oxygen', 'oxygen-equipment'),
        [
            ('Use the facility’s purchase specification', 'If your healthcare procurement request specifies a Dura cylinder, include the required format or capacity and any reference from the existing supply agreement. Share the expected consumption and identify the facility receiving the delivery.'),
            ('Give the site contact and delivery schedule', 'Provide the procurement and receiving contacts, facility location and preferred delivery window. In an enquiry covering multiple wards or facilities, state which location will receive each order.'),
            ('List supporting documents', 'Share the documentation requested by your facility before ordering. If a tender allows an alternative format, provide the tender specification so availability and documentation can be discussed against it.'),
        ],
    ),
    'argon-for-tig-welding': (
        'Argon Cylinder Enquiries for TIG Welding in Kerala',
        'Request argon for TIG welding. Include the gas specified by your welding procedure, cylinder size and delivery location.',
        'argon', 'fabrication', ('argon', 'helium'),
        [
            ('Follow the shielding gas specification', 'Argon is used as a shielding gas in some TIG welding applications. Locate the gas and grade specified by your procedure before asking for a quote. If the procedure specifies a mixture, provide the full composition and any grade requirement.'),
            ('Estimate demand by workstation', 'Include the number of welders or stations using cylinders, how long the job will run and your usual cylinder usage. If more than one procedure is in use, list orders for different grades or mixtures separately.'),
            ('Share the cylinder and job details', 'Give the specified cylinder size or valve connection and planned job start. For a regular exchange, share the delivery address, available receiving hours and typical order size.'),
        ],
    ),
    'carbon-dioxide-for-beverages': (
        'Carbon Dioxide Enquiries for Beverage Carbonation',
        'Enquire about CO₂ for beverage carbonation in Kerala. Share your required grade, documentation and whether you need cylinder or liquid supply.',
        'carbon-dioxide', 'cylinder-co2', ('carbon-dioxide', 'nitrogen'),
        [
            ('Collect the quality details first', 'Use your beverage plant’s CO₂ purchase specification. Include the relevant grade and the documents your food safety or quality team requires for supplier approval. Send those details before confirming an order.'),
            ('Describe the receiving setup', 'State whether your site currently orders cylinders or liquid CO₂. Give the required quantity and attach any receiving requirements named by your equipment supplier. For several lines or production sites, identify the quantity for each.'),
            ('Forecast production peaks', 'List weekly usage at typical output and any peaks such as a seasonal run or product launch. Share the lead time you need and when the receiving team can accept the delivery.'),
        ],
    ),
    'helium-leak-detection': (
        'Helium Gas Enquiries for Leak Detection in Kerala',
        'Ask about helium cylinders for specified leak-detection equipment. Supply the instrument details, gas grade, cylinder connection and delivery PIN code.',
        'helium', 'cylinder-helium', ('helium', 'argon'),
        [
            ('Use the test specification', 'Identify the gas grade and impurity requirements listed by the leak detector manufacturer or on the test procedure. If the procedure specifies a mixture, include its complete composition and tolerance rather than quoting only the helium content.'),
            ('Match the cylinder to the equipment', 'Specify the cylinder capacity and connection called for by the instrument or gas system. Include a make and model reference if the gas specification is available in the equipment documentation.'),
            ('Coordinate with the test schedule', 'State whether the request is for a single inspection, a commissioning activity or routine production testing. Include the quantity, test date and the site contact receiving the cylinders.'),
        ],
    ),
}

MALAYALAM_PRODUCTS = {
    'industrial-oxygen': 'വ്യാവസായിക ഓക്സിജൻ',
    'nitrogen': 'നൈട്രജൻ വാതകവും ദ്രാവക നൈട്രജനും',
    'argon': 'ആർഗൺ',
    'carbon-dioxide': 'കാർബൺ ഡൈഓക്സൈഡ്',
    'acetylene': 'അസറ്റിലീൻ',
    'helium': 'ഹീലിയം',
    'medical-oxygen': 'മെഡിക്കൽ ഓക്സിജൻ',
    'oxygen-equipment': 'ഓക്സിജൻ ഉപകരണങ്ങൾ',
    'liquid-nitrogen-equipment': 'ദ്രാവക നൈട്രജൻ സംഭരണ പാത്രങ്ങൾ',
    'dry-ice': 'ഡ്രൈ ഐസ്',
}

MALAYALAM_DISTRICTS = (
    'തിരുവനന്തപുരം', 'കൊല്ലം', 'പത്തനംതിട്ട', 'ആലപ്പുഴ', 'കോട്ടയം', 'ഇടുക്കി', 'എറണാകുളം',
    'തൃശ്ശൂർ', 'പാലക്കാട്', 'മലപ്പുറം', 'കോഴിക്കോട്', 'വയനാട്', 'കണ്ണൂർ', 'കാസർഗോഡ്',
)
