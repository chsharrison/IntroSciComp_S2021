activity <- file.choose() # make sure time of day is in radian format
#Fit without confidence limits
data(activity)
tm <- 2*pi*subset(activity)$time
mod1 <- fitact(tm)
plot(mod1)

#Fit with confidence limits (limited reps to speed up)
mod2 <- fitact(tm, sample="data", reps=100)
plot(mod2)