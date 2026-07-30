local RunService = game:GetService("RunService")
local part = script.Parent

local function getNumberAttribute(obj, name, default)
	local value = obj:GetAttribute(name)
	return typeof(value) == "number" and value or default
end

local forward = true

while true do
	local forwardDist = getNumberAttribute(part, "ForwardDistance", 50)
	local backwardDist = getNumberAttribute(part, "BackwardDistance", 50)
	local speed = getNumberAttribute(part, "Speed", 10) -- studs/sec
	local pause = getNumberAttribute(part, "Pause_Time", 0.2)

	local targetDistance = forward and forwardDist or backwardDist
	local direction = forward and -1 or 1

	local moved = 0

	while moved < targetDistance do
		local dt = RunService.Heartbeat:Wait()
		local move = math.min(speed * dt, targetDistance - moved)

		part.CFrame *= CFrame.new(0, 0, direction * move)
		moved += move
	end

	forward = not forward
	task.wait(pause)
end
