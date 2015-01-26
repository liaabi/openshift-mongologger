from setuptools import setup

setup(name='OpenShift Mongo Twt',
      version='1.0',
      description='OpenShift Logger in MongoDB',
      author='liaabi',
      author_email='ligia.arghir@cloudandheat.com',
      url='https://github.com/liaabi/openshift-mongologger.git',
      # dont install bottle requirement, bottle is included in source
      install_requires=['pymongo'],
     )
