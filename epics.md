
3 types of messages, commands, events + queries - event storming

All models are wrong, some are useful
CQRS Architecture

Query Model is built to answer my question
e.g. I need the median price over 200 days
e.g. API Get close price, get the length of time 

Command model - an instruction to do something (commands for system activity)
Command handler recieves command 
Command handler validates command
Command handler processes the command 
Event is fired for every action you are interested in
may be several events for a command
Event Handler/Listener will make the state change


This will update the table
Any 

Query model is listenining for 



# EPIC 1 - Univariate etf analysis
Descriptive statistics - Mean
relative frequency Histogram - (i) vs f(i)/n
frequency density histogram - (i) vs f(i)/n(c(i) - c(i-1)) where c(i) - c(i-1) is the class width

EPIC 1
close price
Median
Standard deviation
percentage returns


1 Mock data in form that front end requires
Once I validate it we know what form the API needs to provide data
 


# EPIC 2 - Bivariate
Pairwise correlation

suprise = Return - average return (100 or 200 day) / typical return size

# EPIC 3 - Multivariate