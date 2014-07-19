OpenShift - Twt Mongo Demo for MongoDB RS

This repository is designed to be used with https://www.openshift.com
applications.  To use, just follow the quickstart below.

Quickstart
==========

1) Create an account at https://www.openshift.com

2) Create a python application with mongodb-ha:

    rhc app create twt python-2.7 mongodb-ha

3) Add this upstream repo

    cd twt
    git remote add upstream -m master git://github.com/liaabi/openshift-twt-mongo-demo.git
    git pull -s recursive -X theirs upstream master

4) Then push the repo upstream

    git push

5) That's it, you can now browse to your application at:

    http://twt-$yournamespace.rhcloud.com

License
-------

This code is dedicated to the public domain to the maximum extent
permitted by applicable law, pursuant to CC0
http://creativecommons.org/publicdomain/zero/1.0/
