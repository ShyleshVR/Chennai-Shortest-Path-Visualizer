import turtle
from ShortestPath import shortest_path
from PlotLocation import scale_coordinates, plot_locations
from Data import dist, coordinates

source_node = input("Enter your source : ")
destination_node = input("Enter your destination : ")
shortest_path_nodes = shortest_path(dist, source_node, destination_node)
plot_locations(coordinates,shortest_path_nodes)


