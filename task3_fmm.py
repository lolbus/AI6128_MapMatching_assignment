from fmm import FastMapMatch,Network,NetworkGraph,UBODTGenAlgorithm,UBODT,FastMapMatchConfig
network_name = "porto_whole1"
Dir = "./" + network_name + "/"
network = Network(Dir+"edges.shp","fid","u","v")
print "Nodes {} edges {}".format(network.get_node_count(),network.get_edge_count())
graph = NetworkGraph(network)



# Can be skipped if you already generated an ubodt file
ubodt_gen = UBODTGenAlgorithm(network,graph)
status = ubodt_gen.generate_ubodt(Dir+"ubodt.txt", 0.03, binary=False, use_omp=True)
print status

### Read UBODT
ubodt = UBODT.read_ubodt_csv(Dir+"ubodt.txt")
### Create FMM model
fmm_model = FastMapMatch(network,graph,ubodt)


k = 8
radius = 0.003
gps_error = 0.0005
fmm_config = FastMapMatchConfig(k,radius,gps_error)


#RUN MAP MATCH

wkt = "LINESTRING(-8.618643 41.141412,-8.618499 41.141376,-8.620326 41.14251,-8.622153 41.143815,-8.623953 41.144373,-8.62668 41.144778,-8.627373 41.144697,-8.630226 41.14521,-8.632746 41.14692,-8.631738 41.148225,-8.629938 41.150385,-8.62911 41.151213,-8.629128 41.15124,-8.628786 41.152203,-8.628687 41.152374,-8.628759 41.152518,-8.630838 41.15268,-8.632323 41.153022,-8.631144 41.154489,-8.630829 41.154507,-8.630829 41.154516,-8.630829 41.154498,-8.630838 41.154489)"
result = fmm_model.match_wkt(wkt,fmm_config)

### Print map matching result
print "Opath ",list(result.opath)
print "Cpath ",list(result.cpath)
print "WKT ",result.mgeom.export_wkt()

from fmm import GPSConfig,ResultConfig

# Define input data configuration
input_config = GPSConfig()
input_config.file = Dir+"trips_time.txt"
input_config.id = "id"
input_config.GPS_point = True
print input_config.to_string()

# Define output configuration
result_config = ResultConfig()
result_config.file = Dir+ network_name + "_output.txt"
result_config.output_config.write_opath = True
print result_config.to_string()

status = fmm_model.match_gps_file(input_config, result_config, fmm_config, use_omp = True)
print status