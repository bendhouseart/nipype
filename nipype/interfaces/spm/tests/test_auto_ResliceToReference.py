# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import ResliceToReference


def test_ResliceToReference_inputs():
    input_map = dict(
        bounding_box=dict(field='comp{2}.idbbvox.bb', ),
        in_files=dict(
            field='fnames',
            mandatory=True,
        ),
        interpolation=dict(field='interp', ),
        matlab_cmd=dict(),
        mfile=dict(usedefault=True, ),
        paths=dict(),
        target=dict(
            extensions=None,
            field='comp{1}.id.space',
        ),
        use_mcr=dict(),
        use_v8struct=dict(
            min_ver='8',
            usedefault=True,
        ),
        voxel_sizes=dict(field='comp{2}.idbbvox.vox', ),
    )
    inputs = ResliceToReference.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_ResliceToReference_outputs():
    output_map = dict(out_files=dict(), )
    outputs = ResliceToReference.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
