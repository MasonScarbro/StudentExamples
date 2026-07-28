local ServerStorage = game:GetService("ServerStorage")
local Players = game:GetService("Players")

local moduleScripts = ServerStorage:WaitForChild("ModuleScripts")
local matchManager = require(moduleScripts:WaitForChild("MatchManager"))
local gameSettings = require(moduleScripts:WaitForChild("GameSettings"))

while true do
	repeat
		task.wait(gameSettings.intermissionDuration)
		print("Restarting Intermission")
	until
	
	print("Intermission Over")
	task.wait(gameSettings.transitionTime)
	
	matchManager.prepareGame()
end
