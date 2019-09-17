# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..model import SMM


def test_SMM_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        mask=dict(
            argstr='--mask="%s"',
            copyfile=False,
            extensions=None,
            mandatory=True,
            position=1,
        ),
        no_deactivation_class=dict(
            argstr='--zfstatmode',
            position=2,
        ),
        output_type=dict(),
        spatial_data_file=dict(
            argstr='--sdf="%s"',
            copyfile=False,
            extensions=None,
            mandatory=True,
            position=0,
        ),
    )
    inputs = SMM.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_SMM_outputs():
    output_map = dict(
        activation_p_map=dict(extensions=None, ),
        deactivation_p_map=dict(extensions=None, ),
        null_p_map=dict(extensions=None, ),
    )
    outputs = SMM.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
