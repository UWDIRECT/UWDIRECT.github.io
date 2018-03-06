import sys

x = ["x1", "x2", "x3"]
l1 = ["l1_1", "l1_2", "l1_3"]
l2d1 = ["l2_1d", "l2_2", "l2_3d", "l2_4", "l2_5d", "l2_6"]
l2d2 = ["l2_1", "l2_2d", "l2_3", "l2_4d", "l2_5", "l2_6d"]
l2d3 = ["l2_1", "l2_2d", "l2_3d", "l2_4d", "l2_5", "l2_6"]
o = ["o1", "o2"]

preamble_pre = """
digraph G {

        rankdir=LR
	    splines=line
        nodesep=.05;
        
        node [label=""];
"""
preamble_0 = """

        subgraph cluster_0 {
		color=white;
                node [style=solid,color=blue4, shape=circle];
		label = "inputs";
"""
preamble_1 = """
	}

	subgraph cluster_1 {
		color=white;
		node [style=solid,color=cyan, shape=circle];
		label = "layer 1";
"""
preamble_2 = """
	}

	subgraph cluster_2 {
		color=white;
		node [style=solid,color=magenta, shape=circle];
		label = "layer 2";
"""
preamble_3 = """
	}

	subgraph cluster_3 {
		color=white;
		node [style=solid,color=black, shape=circle];
		label="output";
"""
preamble_post = """
	}
"""

postfix="""
}
"""

def layer_connect(l1, l2, f=sys.stdout):
    for i in l1:
        for j in l2:
            if i.endswith('d') or j.endswith('d'):
                print("    %s -> %s [style=dotted]" % (i, j), file=f)
            else:
                print("    %s -> %s" % (i, j), file=f)

def generate_preamble(filename, layers):
    with open(filename, 'w', encoding='utf-8') as f:
        print(preamble_pre, file=f)
        print(preamble_0, file=f)
        for node in layers[0]:
            if node.endswith('d'):
                print("        %s [style=dotted]" % node, file=f)
            else:
                print("        %s" % node, file=f)
        print(preamble_1, file=f)
        for node in layers[1]:
            if node.endswith('d'):
                print("        %s [style=dotted]" % node, file=f)
            else:
                print("        %s" % node, file=f)
        print(preamble_2, file=f)
        for node in layers[2]:
            if node.endswith('d'):
                print("        %s [style=dotted]" % node, file=f)
            else:
                print("        %s" % node, file=f)
        print(preamble_3, file=f)
        for node in layers[3]:
            if node.endswith('d'):
                print("        %s [style=dotted]" % node, file=f)
            else:
                print("        %s" % node, file=f)
        print(preamble_post, file=f)


def generate_graph(filename, layers):
    generate_preamble(filename, layers)
    with open(filename, 'a', encoding='utf-8') as f:
        l = len(layers)
        for i in range(l-1):
            layer_connect(layers[i], layers[i+1], f)
        print(postfix, file=f)

generate_graph("dropout1.dot", [x, l1, l2d1, o])
generate_graph("dropout2.dot", [x, l1, l2d2, o])
generate_graph("dropout3.dot", [x, l1, l2d3, o])
