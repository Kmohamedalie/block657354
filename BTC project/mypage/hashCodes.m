T = readtable('hashCode.csv'); %import csv file

maxVal = max(T.inputs);  %finding the maximum value transacted in the block
minVal = min(T.inputs);     %finding the minimum value value transacted in the block
avgValue = mean(T.inputs); %finding the average value transacted in the block

           %Code for graphical display
hold  on %add anothe plot           
plot(T.inputs,'k')  %displaying the plots
plot(1373,maxVal,'r*') %plotting a red star to indicting the max value
grid on % adding grid to the plot
ylabel('Value of BTC') %naming the y-axis
xlabel('Index') %naming the x-axis
title('Graphical display of the values') % main title of our plot





%statistical analysis
MAXval = 'The maximum value transacted is: ';
MINval ='The minimum value transacted is: ';
AVGval = ' The average amount of value transacted is: ';

disp(MAXval) %print out the variable for the max value
disp(maxVal)


disp(MINval) %print out the variable for the min value
disp(minVal)


disp(AVGval) %print out the variable for the average value
disp(avgValue)



