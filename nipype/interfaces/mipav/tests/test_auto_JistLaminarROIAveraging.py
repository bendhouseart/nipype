# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..developer import JistLaminarROIAveraging


def test_JistLaminarROIAveraging_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inIntensity=dict(
            argstr='--inIntensity %s',
            extensions=None,
        ),
        inMask=dict(
            argstr='--inMask %s',
            extensions=None,
        ),
        inROI=dict(
            argstr='--inROI %s',
            extensions=None,
        ),
        inROI2=dict(argstr='--inROI2 %s', ),
        null=dict(argstr='--null %s', ),
        outROI3=dict(
            argstr='--outROI3 %s',
            hash_files=False,
        ),
        xDefaultMem=dict(argstr='-xDefaultMem %d', ),
        xMaxProcess=dict(
            argstr='-xMaxProcess %d',
            usedefault=True,
        ),
        xPrefExt=dict(argstr='--xPrefExt %s', ),
    )
    inputs = JistLaminarROIAveraging.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_JistLaminarROIAveraging_outputs():
    output_map = dict(outROI3=dict(extensions=None, ), )
    outputs = JistLaminarROIAveraging.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
