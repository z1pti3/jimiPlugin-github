from core import plugin, model

class _github(plugin._plugin):
    version = 0.1

    def install(self):
        # Register models
        model.registerModel("githubGetRateLimit","_githubGetRateLimit","_action","plugins.github.models.action")
        model.registerModel("githubGetLatestCommit","_githubGetLatestCommit","_action","plugins.github.models.action")
        model.registerModel("githubTriggerLatestCommitPoll","_githubTriggerLatestCommitPoll","_trigger","plugins.github.models.trigger")
        return True

    def uninstall(self):
        # deregister models
        model.deregisterModel("githubGetRateLimit","_githubGetRateLimit","_action","plugins.github.models.action")
        model.deregisterModel("githubGetLatestCommit","_githubGetLatestCommit","_action","plugins.github.models.action")
        model.deregisterModel("githubTriggerLatestCommitPoll","_githubTriggerLatestCommitPoll","_trigger","plugins.github.models.trigger")
        return True

