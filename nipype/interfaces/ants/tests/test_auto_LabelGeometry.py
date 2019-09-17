# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import LabelGeometry


def test_LabelGeometry_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        dimension=dict(
            argstr='%d',
            position=0,
            usedefault=True,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        intensity_image=dict(
            argstr='%s',
            extensions=None,
            mandatory=True,
            position=2,
            usedefault=True,
        ),
        label_image=dict(
            argstr='%s',
            extensions=None,
            mandatory=True,
            position=1,
        ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        output_file=dict(
            argstr='%s',
            name_source=['label_image'],
            name_template='%s.csv',
            position=3,
        ),
    )
    inputs = LabelGeometry.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_LabelGeometry_outputs():
    output_map = dict(output_file=dict(extensions=None, ), )
    outputs = LabelGeometry.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
