clear all
clc

log1 = importdata('log1.txt');
%current =log1(0.5e5:end,1);
current_voltage = log1(0.5e5:end,1:2);
arc = log1(0.5e5:end,3);

log2=importdata('log2.txt');
%current2 =log2(0.5e5:end,1);
current_voltage2 = log2(0.5e5:end,1:2);
arc2 = log2(0.5e5:end,3);

log3=importdata('log3.txt');
current_voltage3 = log3(0.5e5:end,1:2);
arc3 = log3(0.5e5:end,3);

% evaluate this selection one by one because cell2mat fails
save('all_voltages', 'current_voltage', 'current_voltage2', 'current_voltage3');
all_voltages=load('all_voltages.mat');
all_voltages=struct2cell(all_voltages);
all_voltages=cell2mat(all_voltages);

save('all_arcs', 'arc', 'arc2', 'arc3');
all_arcs=load('all_arcs.mat');
all_arcs=struct2cell(all_arcs);
all_arcs=cell2mat(all_arcs);

%output=load('nnet_3files_output.mat');
%output=struct2cell(output);
%output=cell2mat(output);

%delay 
xi1 = all_voltages(1:10, 1:2);
xi2 = all_arcs(1:10);

[y1,xf1] = myNeuralNetworkFunction_io(all_voltages.',xi1.');

%plot network output against actual arc
figure(12)
plot(1:length(y1),all_arcs,1:length(y1),y1)


%testing the network on new data
log4 = importdata('log4.txt');
current_voltage4 = log4(0.5e5:end,1:2);
arc4 = log4(0.5e5:end,3);

%delays for new data
xi1_test = current_voltage4(1:10, 1:2);
xi2_test = arc4(1:10);

[y_new,xf1_new] = myNeuralNetworkFunction_io(current_voltage4.',xi1_test.');

%plot network output against actual arc
figure(12)
plot(1:length(y_new),arc4,1:length(y_new),y_new)


%save('current.mat','current', 'current2');
%currents=load('current.mat');

 %plot(1:length(arc2),arc(1:length(arc2)),1:length(arc2),arc2)
 
 
