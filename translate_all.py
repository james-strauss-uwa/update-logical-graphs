import os
import subprocess

GRAPH_LIST = [
    "daliuge-logical-graphs/ARL Examples/dlg_arl_demo.json",
    "daliuge-logical-graphs/ARL Examples/imaging_single_node.json",
    "daliuge-logical-graphs/ARL Examples/imaging.json",

    "daliuge-logical-graphs/ASKAP Pipelines/askap_dingo_expanded.json",
    "daliuge-logical-graphs/ASKAP Pipelines/askap_dingo.json",
    "daliuge-logical-graphs/ASKAP Pipelines/askap_hello.json",
    "daliuge-logical-graphs/ASKAP Pipelines/askap_LoadParset.json",
    "daliuge-logical-graphs/ASKAP Pipelines/askap_LoadVis.json",
    "daliuge-logical-graphs/ASKAP Pipelines/askap_SolveNE.json",
    "daliuge-logical-graphs/ASKAP Pipelines/askap_SpectralLine.json",
    "daliuge-logical-graphs/ASKAP Pipelines/askap_TestCube.json",
    "daliuge-logical-graphs/ASKAP Pipelines/askap_TestSingleChannel.json",
    "daliuge-logical-graphs/ASKAP Pipelines/askap_TestTwoChannel.json",

    "daliuge-logical-graphs/ATCA Pipelines/atca_attila.json",
    "daliuge-logical-graphs/ATCA Pipelines/atca_minh.json",
    "daliuge-logical-graphs/ATCA Pipelines/richard.json",

    "daliuge-logical-graphs/CHILES Pipelines/chiles_imaging.json",
    "daliuge-logical-graphs/CHILES Pipelines/chiles_simple.json",
    "daliuge-logical-graphs/CHILES Pipelines/chiles_two_dev1.json",
    "daliuge-logical-graphs/CHILES Pipelines/chiles_two_dev2.json",
    "daliuge-logical-graphs/CHILES Pipelines/chiles_two.json",

    "daliuge-logical-graphs/LOFAR Pipelines/CALIB.json",
    "daliuge-logical-graphs/LOFAR Pipelines/lofar_cal.json",
    "daliuge-logical-graphs/LOFAR Pipelines/lofar_std.json",
    "daliuge-logical-graphs/LOFAR Pipelines/prefactor.json",

    "daliuge-logical-graphs/MWA Pipelines/mwa_gleam_simple.json",
    "daliuge-logical-graphs/MWA Pipelines/mwa_gleam.json",
    "daliuge-logical-graphs/MWA Pipelines/mwa_pipeline_simple.json",
    "daliuge-logical-graphs/MWA Pipelines/mwa_pipeline.json",

    "daliuge-logical-graphs/SageCal/dist_sagecal_dynlib.json",
    "daliuge-logical-graphs/SageCal/dist_sagecal.json",

    "daliuge-logical-graphs/Scalability tests/lofar_nsm_2x4.json",
    "daliuge-logical-graphs/Scalability tests/lofar_nsm_256x512.json",
    "daliuge-logical-graphs/Scalability tests/lofar_nsm_512x512.json",
    "daliuge-logical-graphs/Scalability tests/lofar_nsm_512x1024.json",
    "daliuge-logical-graphs/Scalability tests/lofar_nsm_768x1024.json",
    "daliuge-logical-graphs/Scalability tests/lofar_nsm_1024x1024.json",
    "daliuge-logical-graphs/Scalability tests/lofar_nsm_1024x2048.json",
    "daliuge-logical-graphs/Scalability tests/lofar_nsm_2048x2048.json",
    "daliuge-logical-graphs/Scalability tests/lofar_nsm_2048x5120.json",
    "daliuge-logical-graphs/Scalability tests/lofar_test_2x4.json",
    "daliuge-logical-graphs/Scalability tests/lofar_test_4x4.json",
    "daliuge-logical-graphs/Scalability tests/lofar_test_4x8.json",
    "daliuge-logical-graphs/Scalability tests/lofar_test_8x8.json",
    "daliuge-logical-graphs/Scalability tests/lofar_test_8x16.json",
    "daliuge-logical-graphs/Scalability tests/lofar_test_16x16.json",
    "daliuge-logical-graphs/Scalability tests/lofar_test_16x32.json",
    "daliuge-logical-graphs/Scalability tests/lofar_test_32x32.json",
    "daliuge-logical-graphs/Scalability tests/lofar_test_32x64.json",
    "daliuge-logical-graphs/Scalability tests/lofar_test_64x64.json",
    "daliuge-logical-graphs/Scalability tests/lofar_test_64x128.json",
    "daliuge-logical-graphs/Scalability tests/lofar_test_128x128.json",
    "daliuge-logical-graphs/Scalability tests/lofar_test_128x256.json",
    "daliuge-logical-graphs/Scalability tests/lofar_test_256x256.json",
    "daliuge-logical-graphs/Scalability tests/lofar_test_256x512.json",

    "daliuge-logical-graphs/SDP PIP Pipelines/MS-MSF_Fc-Fq-Ti-Sb.json",
    "daliuge-logical-graphs/SDP PIP Pipelines/MS-MSF_Fc-Ti-Fq-Sb.json",
    "daliuge-logical-graphs/SDP PIP Pipelines/MS-MSF_Fq-Fc-Ti-Sb.json",
    "daliuge-logical-graphs/SDP PIP Pipelines/MS-MSF_Fq-Ti-Fc-Sb.json",
    "daliuge-logical-graphs/SDP PIP Pipelines/MS-MSF_Ti-Fc-Fq-Sb.json",
    "daliuge-logical-graphs/SDP PIP Pipelines/MS-MSF_Ti-Fq-Fc-Sb.json",

    "daliuge-logical-graphs/SDP Pipelines/cont_img.json",
    "daliuge-logical-graphs/SDP Pipelines/dist_sagecal_sleep.json",
    "daliuge-logical-graphs/SDP Pipelines/dist_sagecal.json",
    "daliuge-logical-graphs/SDP Pipelines/facet_img.json",
    "daliuge-logical-graphs/SDP Pipelines/fast_cont_img.json",
    "daliuge-logical-graphs/SDP Pipelines/ingest.json",
    "daliuge-logical-graphs/SDP Pipelines/spec_img.json",

    "daliuge-logical-graphs/Tests/bash_test_02.json",
    "daliuge-logical-graphs/Tests/bash_test.json",
    "daliuge-logical-graphs/Tests/dynlib_test.json",
    "daliuge-logical-graphs/Tests/fits_example.json",
    "daliuge-logical-graphs/Tests/simple_test_500.json",
    "daliuge-logical-graphs/Tests/simple_test_1000.json",
    "daliuge-logical-graphs/Tests/simple_test_2000.json",
    "daliuge-logical-graphs/Tests/test_grpby_gather.json",
    "daliuge-logical-graphs/Tests/test_grpby_in_scatter.json",
    "daliuge-logical-graphs/Tests/test_mk_grpby.json",
    "daliuge-logical-graphs/Tests/test_seq_gather.json",
    "daliuge-logical-graphs/Tests/test_stream_multiple.json",
    "daliuge-logical-graphs/Tests/test_stream.json",

    "EAGLE_test_repo/SP-602/YAN-251-001.graph",
    "EAGLE_test_repo/SP-602/YAN-251-001.palette",

    "EAGLE_test_repo/dingo/dingo.graph",
    "EAGLE_test_repo/dingo/dingo.palette",
    "EAGLE_test_repo/dingo/dingo_output_param.graph",
    "EAGLE_test_repo/dingo/mock-dingo.graph",
    "EAGLE_test_repo/dingo/test_exclusive.graph",

    "EAGLE_test_repo/simple_tests/simple.palette",
    "EAGLE_test_repo/simple_tests/simple_01_basic.graph",
    "EAGLE_test_repo/simple_tests/simple_02_mkn.graph",
    "EAGLE_test_repo/simple_tests/simple_03_mkn_plus_fen.graph",

    "EAGLE_test_repo/wsclean/wsclean.graph",

    "EAGLE_test_repo/CImage.graph",
    "EAGLE_test_repo/CImage.palette",

    "EAGLE_test_repo/ChilesSplitDeploy.graph",
    "EAGLE_test_repo/Chiles.palette",

    "EAGLE_test_repo/LEAP-Work-Flow.graph",
    "EAGLE_test_repo/LEAP-Work-Flow.palette",

    "EAGLE_test_repo/SummitIngest_Demo.graph",

    "EAGLE_test_repo/HelloWorld.json.graph",
    "EAGLE_test_repo/HelloWorld.palette",

    "EAGLE_test_repo/defaultTemplate.palette",

    "summit_demo/lgs/summit_oskar2_006_nodes.json",
    "summit_demo/lgs/summit_oskar2_024_nodes.json",
    "summit_demo/lgs/summit_oskar2_096_nodes.json",
    "summit_demo/lgs/summit_oskar2_384_nodes.json",
    "summit_demo/lgs/summit_oskar2_1536_nodes.json",
    "summit_demo/lgs/summit_oskar2_6144_nodes.json",
    "summit_demo/lgs/test_stats.graph",
]

OUTPUT_DIR = "output"
TRANSLATE_SCRIPT_DIR = "../EAGLE/tools"

for graph_filename in GRAPH_LIST:
    # get full path
    full_path = os.path.join(os.getcwd(), "../", graph_filename)

    # create output file name
    output_filename = os.path.join(os.getcwd(), OUTPUT_DIR, graph_filename)

    # check input file exists
    exists = os.path.exists(full_path)

    if not exists:
        print("ERROR: File " + full_path + " does not exist! Aborting.")
        break

    # if output dir does not exist, create it
    output_directory = os.path.dirname(output_filename)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    print(full_path + " -> " + output_filename)

    #continue

    #DEVNULL
    DEVNULL = open(os.devnull, 'w')

    # call the translator script
    process = subprocess.call(['ts-node', 'updateGraph.ts', full_path, output_filename], cwd=TRANSLATE_SCRIPT_DIR, stdout=DEVNULL)
