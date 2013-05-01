spaceappsdatahacks
==================

Short description
-----------------

Bits and pieces hacked together for SpaceApps

Long description
----------------

Python scripts to harvest data from JPL HORIZONS files and the Planetary Data
System image archive for the SpaceApps Challenge:

* conv.py : Quick conversion of JPL HORIZONS spacecraft ephemeris to 
list-of-lists (date, X and Y only)
* getimgurl.py : find first GEOMETRICALLY_CORRECTED object image in Voyager
INDEX.TAB file and construct a URL to the BROWSEable JPG in PDS.
* getimgurl3.py : better version, with fixes and output of time, date, object.
* getind.py : download INDEX.TAB files for the Voyager data.

TODO
----

* proper handling of all Voyager data (not just "Browse" images)
* rewrite as functions for inclusion into other programs
* expand to all mission archives in PDS (other formats/directory layouts?)

References
==========

* [SpaceView project page](http://spaceappschallenge.org/project/spaceview/)
* [NASA HORIZONS page](http://ssd.jpl.nasa.gov/?horizons)
* [NASA HORIZONS User Manual](http://ssd.jpl.nasa.gov/?horizons_doc)
* [NASA PDS raw data](http://pds-rings.seti.org/volumes/)
