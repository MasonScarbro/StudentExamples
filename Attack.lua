local PathfindingService = game:GetService("PathfindingService")

local boss = script.Parent
local humanoid = boss:WaitForChild("Humanoid")
local root = boss:WaitForChild("HumanoidRootPart")
local animator = humanoid:WaitForChild("Animator")

local walkAnimation = Instance.new("Animation")
walkAnimation.AnimationId = "rbxassetid://507777826" 

local walkTrack = animator:LoadAnimation(walkAnimation)
walkTrack.Looped = true
walkTrack.Priority = Enum.AnimationPriority.Movement
local DAMAGE = 20
local ATTACK_RANGE = 6
local ATTACK_COOLDOWN = 1

local lastAttack = 0

while true do
	local closestPlayer = nil
	local closestDistance = math.huge

	-- Find nearest player
	for _, player in ipairs(game.Players:GetPlayers()) do
		local character = player.Character

		if character
			and character:FindFirstChild("HumanoidRootPart")
			and character:FindFirstChild("Humanoid")
			and character.Humanoid.Health > 0 then

			local distance = (character.HumanoidRootPart.Position - root.Position).Magnitude

			if distance < closestDistance then
				closestDistance = distance
				closestPlayer = character
			end
		end
	end

	if closestPlayer then
		local targetRoot = closestPlayer.HumanoidRootPart

		if closestDistance <= ATTACK_RANGE then
			if tick() - lastAttack >= ATTACK_COOLDOWN then
				closestPlayer.Humanoid:TakeDamage(DAMAGE)
				lastAttack = tick()
			end
		else
			humanoid:MoveTo(targetRoot.Position)
			if not walkTrack.IsPlaying then
				walkTrack:Play()
			end
		end
	end

	task.wait(0.1)
end
