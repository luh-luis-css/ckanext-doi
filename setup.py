from setuptools import setup, find_packages

version = '0.2'

setup(
	name='ckanext-doi',
	version=version,
	description='CKAN extension for assigning a DOI to datasets',
	classifiers=[],
	keywords='',
	author='Ben Scott',
	author_email='ben@benscott.co.uk',
	url='',
	license='',
    packages=find_packages(exclude=['tests']),
    namespace_packages=['ckanext', 'ckanext.doi'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'requests',
		'xmltodict'
	],
	entry_points=\
	"""
    [ckan.plugins]
    	doi=ckanext.doi.plugin:DOIPlugin
     [babel.extractors]
        ckan = ckan.lib.extract:extract_ckan
    [paste.paster_command]
        doi=ckanext.doi.commands.doi:DOICommand
	""",
	message_extractors={
		'ckanext': [
			('**.py', 'python', None),
			('**.js', 'javascript', None),
			('**/templates/**.html', 'ckan', None),
		],
	}
)