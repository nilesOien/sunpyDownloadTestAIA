#!/usr/bin/env python

# Test the ability to download the AIA files to track an active region as per
# https://docs.sunpy.org/en/latest/generated/gallery/map/track_active_region.html
#
# Niles Oien December 2025

import astropy.units as u

from sunpy.net import Fido
from sunpy.net import attrs as a

import os
import shutil

# This should create the directory ./data and put the files in it.
# At this level, just test that the directory exists.
def test_dir() :
    query = Fido.search(a.Time('2018-05-30 00:00:00', '2018-05-30 12:00:00'),
                    a.Instrument.aia,
                    a.Wavelength(171*u.angstrom),
                    a.Sample(1*u.h))
    Fido.fetch(query, path='./data')

    assert(os.path.isdir('./data'))

# Test that the expected files exist.
def test_files() :

    expectedFiles = [ { 'filename': 'data/aia.lev1.171A_2018_05_30T00_00_09.35Z.image_lev1.fits'},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T01_00_09.35Z.image_lev1.fits'},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T02_00_09.35Z.image_lev1.fits'},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T03_00_09.35Z.image_lev1.fits'},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T04_00_09.35Z.image_lev1.fits'},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T05_00_09.35Z.image_lev1.fits'},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T06_00_09.35Z.image_lev1.fits'},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T07_00_09.35Z.image_lev1.fits'},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T08_00_09.35Z.image_lev1.fits'},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T09_00_09.35Z.image_lev1.fits'},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T10_00_09.35Z.image_lev1.fits'},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T11_00_09.35Z.image_lev1.fits'} ]

    for file in expectedFiles :
        assert(os.path.isfile(file['filename']))

# Test that the files have the expected sizes.
def test_sizes() :

    expectedFiles = [ { 'filename': 'data/aia.lev1.171A_2018_05_30T00_00_09.35Z.image_lev1.fits', 'filesize': 11517120},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T01_00_09.35Z.image_lev1.fits', 'filesize': 11508480},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T02_00_09.35Z.image_lev1.fits', 'filesize': 11505600},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T03_00_09.35Z.image_lev1.fits', 'filesize': 11502720},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T04_00_09.35Z.image_lev1.fits', 'filesize': 11496960},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T05_00_09.35Z.image_lev1.fits', 'filesize': 11502720},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T06_00_09.35Z.image_lev1.fits', 'filesize': 11508480},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T07_00_09.35Z.image_lev1.fits', 'filesize': 11508480},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T08_00_09.35Z.image_lev1.fits', 'filesize': 11505600},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T09_00_09.35Z.image_lev1.fits', 'filesize': 11505600},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T10_00_09.35Z.image_lev1.fits', 'filesize': 11514240},
                      { 'filename': 'data/aia.lev1.171A_2018_05_30T11_00_09.35Z.image_lev1.fits', 'filesize': 11514240} ]


    for file in expectedFiles :
        assert(os.path.getsize(file['filename']) == file['filesize'])

# Clean up after ourselves.
def test_cleanup() :

    assert(os.path.isdir('./data'))
    assert(shutil.rmtree('./data') is None)

