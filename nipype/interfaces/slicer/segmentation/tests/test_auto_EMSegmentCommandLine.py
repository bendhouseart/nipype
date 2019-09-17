# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..specialized import EMSegmentCommandLine


def test_EMSegmentCommandLine_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        atlasVolumeFileNames=dict(argstr='--atlasVolumeFileNames %s...', ),
        disableCompression=dict(argstr='--disableCompression ', ),
        disableMultithreading=dict(argstr='--disableMultithreading %d', ),
        dontUpdateIntermediateData=dict(
            argstr='--dontUpdateIntermediateData %d', ),
        dontWriteResults=dict(argstr='--dontWriteResults ', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        generateEmptyMRMLSceneAndQuit=dict(
            argstr='--generateEmptyMRMLSceneAndQuit %s',
            hash_files=False,
        ),
        intermediateResultsDirectory=dict(
            argstr='--intermediateResultsDirectory %s', ),
        keepTempFiles=dict(argstr='--keepTempFiles ', ),
        loadAtlasNonCentered=dict(argstr='--loadAtlasNonCentered ', ),
        loadTargetCentered=dict(argstr='--loadTargetCentered ', ),
        mrmlSceneFileName=dict(
            argstr='--mrmlSceneFileName %s',
            extensions=None,
        ),
        parametersMRMLNodeName=dict(argstr='--parametersMRMLNodeName %s', ),
        registrationAffineType=dict(argstr='--registrationAffineType %d', ),
        registrationDeformableType=dict(
            argstr='--registrationDeformableType %d', ),
        registrationPackage=dict(argstr='--registrationPackage %s', ),
        resultMRMLSceneFileName=dict(
            argstr='--resultMRMLSceneFileName %s',
            hash_files=False,
        ),
        resultStandardVolumeFileName=dict(
            argstr='--resultStandardVolumeFileName %s',
            extensions=None,
        ),
        resultVolumeFileName=dict(
            argstr='--resultVolumeFileName %s',
            hash_files=False,
        ),
        targetVolumeFileNames=dict(argstr='--targetVolumeFileNames %s...', ),
        taskPreProcessingSetting=dict(
            argstr='--taskPreProcessingSetting %s', ),
        verbose=dict(argstr='--verbose ', ),
    )
    inputs = EMSegmentCommandLine.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_EMSegmentCommandLine_outputs():
    output_map = dict(
        generateEmptyMRMLSceneAndQuit=dict(extensions=None, ),
        resultMRMLSceneFileName=dict(extensions=None, ),
        resultVolumeFileName=dict(extensions=None, ),
    )
    outputs = EMSegmentCommandLine.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
