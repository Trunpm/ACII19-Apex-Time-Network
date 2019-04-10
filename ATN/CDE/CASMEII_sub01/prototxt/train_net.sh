#!/usr/bin/env sh
set -e
export PYTHONPATH=$PYTHONPATH:/home/XXXX/caffe-master/python
export PYTHONPATH=$PYTHONPATH:/Data/Add_python_layers

/home/XXXX/caffe-master/build/tools/caffe train --solver=ATN/CDE/CASMEII_sub01/prototxt/solver.prototxt --weights=Data/facia_expression_iter_50000.caffemodel --gpu 1
