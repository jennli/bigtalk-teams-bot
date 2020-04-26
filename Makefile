deploy:
	az webapp deployment source config-zip --resource-group "juniper-infra-teams-bot" --name "juniper1-bigtalk-teams-bot-webapp" --src ./bot.zip
