# The Communication Performance of BCDC Data Center Network
>For a more specific definition and experimental results of Data Center Network BCDC, please refer to The paper "The Communication Performance of BCDC Data Center Network"

## Table of contents
- [The experiment purpose](#the-experiment-purpose)
- [Data communication](#data-communication)
- [Fault tolerant performance](#fault-tolerant-performance)
- [Disjunct paths](#disjunct-paths)



### The experiment purpose
Build a network of BCDC data centers from 12 computers. Previous research on this data center network is basically based on theoretical research. Therefore, this project is to test the actual performance of the BCDC network. The python language is mainly used to test the data communication, fault-tolerant performance and disjunction performance of BCDC network. The following is a brief description of the physical and logical structure of the 12 BCDC.

<div align=center><img src="images/data communication.jpg" width = "500" height = "250"  /></div>

>In this project, you will probably see many folders with the same name. This is a different version of what I was doing at the time. Please refer to the documentation in the folder for details.


### Data communication
In this experiment, we conduct one-to-one, one-to-two, one-to-four, one-to-eight, one-to-eleven(broadcast), and eleven to eleven(all-to-all) experiments of 𝑨_3, 𝑫𝑪𝒆𝒍𝒍 and Fat-Tree, respectively. We intend to send 5G data from one source server to all other destination servers and measure the total transmission time and the average CPU usage rate of the server to evaluate the communication performance of these three data center networks. As shown in the figure, the green nodes represent the source nodes that send the data, and the red nodes represent the nodes that receive the data. The following example shows one-to-one and one-to-three data transmission.

<div align=center><img src="images/data communication.png" width = "500" height = "250"  /></div>


### Fault tolerant performance
In second experiment, we will experiment with fault-tolerant routing for 𝑨_3, 𝑫𝑪𝒆𝒍𝒍 and Fat-Tree, including server fault tolerance, switch fault tolerance, link fault tolerance, and hybrid fault tolerance. We intend to send 5G data from one source server to another destination server and measure the data transfer rate per second and the average CPU usage rate of the server to evaluate the communication performance of these three data center networks. The following figure represents server fault tolerance and hybrid fault tolerance, respectively.

<div align=center><img src="images/fault tolerance.png" width = "500" height = "250"  /></div>


### Disjunct paths
Build a network of BCDC data centers from 12 computers. Previous research on this data center network is basically based on theoretical research. Therefore, this project is to test the actual performance of the BCDC network. The python language is mainly used to test the data communication, fault-tolerant performance and disjunction performance of BCDC network. The following is a brief description of the physical and logical structure of the 12 BCDC.

<div align=center><img src="images/disjoint paths.png" width = "500" height = "250"  /></div>
