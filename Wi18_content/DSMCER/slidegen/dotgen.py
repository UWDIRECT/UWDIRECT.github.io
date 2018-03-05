x = ["x1", "x2", "x3"]
l1 = ["l1_1", "l1_2", "l1_3"]
l2 = ["l2_1", "l2_2", "l2_3", "l2_4"]
o = ["output"]

preamble = """
digraph G {

        rankdir=LR
	    splines=line
        nodesep=.05;
        
        node [label=""];
        
        subgraph cluster_0 {
		color=white;
                node [style=solid,color=blue4, shape=point];
		x1 x2 x3;
		label = "inputs";
	}

	subgraph cluster_1 {
		color=white;
		node [style=solid,color=cyan, shape=circle];
		l1_1 l1_2 l1_3;
		label = "layer 1";
	}

	subgraph cluster_2 {
		color=white;
		node [style=solid,color=magenta, shape=circle];
		l2_1 l2_2 l2_3 l2_4;
		label = "layer 2";
	}

	subgraph cluster_3 {
		color=white;
		node [style=solid,color=black, shape=circle];
		o1
		label="output";
	}
"""

postfix="""
}
"""

def layer_connect(l1, l2):
    for i in l1:
        for j in l2:
            print("    %s -> %s" % (i, j))


print(preamble)
layer_connect(x, l1)
layer_connect(l1, l2)
layer_connect(l2, o)
print(postfix)
