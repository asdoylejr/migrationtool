"""
Script to extract metadata from PDFs.
"""
from pyPdf import PdfFileReader

BASEDIR = 'Water_Files/'
#PDFFiles = ['11_wwf_principle_power_weinstein.pdf']

PDFFiles = ['national_hydropower_map.pdf',
'wp_accomplishments_brochure.pdf',
'siting_handbook_2009.pdf',
'riverine_hydrokinetic_resource_assessment_and_mapping.pdf',
'npd_report.pdf',
'national_hydropower_map.pdf',
'mou_offshore_wind_hydrokinetic_deployment.pdf',
'mhk_projects_2013.pdf',
'mhk_factsheet.pdf',
'mappingandassessment.pdf',
'mappingandassessment.pdf',
'hydropower_memorandum_of_understanding.pdf',
'hydropower_memorandum_of_understanding.pdf',
'hydro_climate_change_report.pdf',
'epri_value_hydropower_electric_grid.pdf',
'epri_turbine_effects_on_fish_2012.pdf',
'energy_production_ocean_currents_us.pdf',
'doewater-pnnl-biospec.pdf',
'doewater-14437.pdf',
'doewater-11673.pdf',
'doewater-11263.pdf',
'doewater-10821-pt1.pdf',
'doewater-10753.pdf',
'doewater-102005.pdf',
'doewater-102005.pdf',
'doe_eisa_633b.pdf',
'conv_hydro_projects_2013.pdf',
'amfishsoc-april2007.pdf',
'58363_fs_eere_water.pdf',
'57605.pdf',
'57605.pdf',
'51315.pdf',
'51235.pdf',
'48642.pdf',
'2011_water_power_peer_review_report.pdf',
'2011_water_power_peer_review_agenda.pdf',
'2010_water_power_peer_review_report.pdf',
'2009_water_power_peer_review_report.pdf',
'18_fy09_lab_call_nrel_thresher_v2-1.pdf',
'11_wwf_principle_power_weinstein.pdf',
'1055457.pdf',
'1023527.pdf',
'1023527.pdf',
'28812.pdf',
'http://www.irs.gov/pub/irs-drop/n-13-29.pdf',
'NSD_Methodology_Report.pdf',
'9505_FY12_Assessment_Report.pdf',
]


for file in PDFFiles:
	#pdf_toread = PdfFileReader(open(BASEDIR + file, 'rb'))

	try:
		pdf_toread = PdfFileReader(open(BASEDIR + file, 'rb'))
		pdf_info = pdf_toread.getDocumentInfo()
		print file + "--" + pdf_info['/Title'] + " - " + pdf_info['/Subject']
	except:
		print 'null'
		pass
	
	#print file + "--" + pdf_info['/Title'] + " - " + pdf_info['/Subject']