# Part B + Bonus - OPA
OPA is a tool that separates the evaluation of various policies and the actual execution of these policies. The first benefit that we gain from this separation is that by having a dedicating tool for policy evaluation, we can develop more advanced and universal policies. This universal design also helps in compatibility issues between different components of the application when they must apply rules based on the same policies. Also, communication between different components that implement their own rules and policies (not using OPA) may lead to unwanted security issues.

OPA seems to be a good fit when we need to evaluate different conditions. For example, in the FMS case, we could potentially use OPA to apply different penalties to drivers if they exceed the speed limit. Or it could be used as an Access Control mechanism if we have different roles in the system. Lastly, by extending the application and adding new features we could apply pricing policies based on the time (day/night) or location.

In the case of the current application, OPA could be used for assigning penalty point to drivers. An example of the code can be found below:
```
points = (speed - 60)*1{
	speed := input.speed
    speed >= 60 ; speed < 80
}

points = (speed - 50)*1{
	speed := input.speed
    speed >= 80 ; speed < 100
}

points = (speed - 100)*5{
	speed := input.speed
    speed >= 100 
}
```