from setuptools import setup

if __name__ == '__main__':
    setup(
        package_data={'smart_documentation': 
        [ 
            'Templates/default/Template/docs/*.html',
        ]
        }
    )