echo "Building ROS nodes"

cd Examples/ROS/ORB_SLAM2
mkdir build
cd build
cmake .. -DOpenCV_DIR=/home/auv/software/opencv/build -DROS_BUILD_TYPE=Release
make -j
