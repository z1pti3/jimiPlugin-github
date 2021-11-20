from plugins.github.includes import github

import jimi

class _githubGetRateLimit(jimi.action._action):

    def doAction(self,data):
        githubObj = github._github()
        result = githubObj.getRateLimit()
        if result:
            return { "result" : True, "rc" : 0, "limits" : result }
        return { "result" : False, "rc" : 255, "msg" : "Unexpected result from API call" }


class _githubGetLatestCommit(jimi.action._action):
    owner = str()
    repo = str()

    def doAction(self,data):
        owner = jimi.helpers.evalString(self.owner,{"data" : data["flowData"],"eventData" : data["eventData"],"conductData" : data["conductData"],"persistentData" : data["persistentData"]})
        repo = jimi.helpers.evalString(self.repo,{"data" : data["flowData"],"eventData" : data["eventData"],"conductData" : data["conductData"],"persistentData" : data["persistentData"]})
        githubObj = github._github()
        result = githubObj.getLatestCommit(owner,repo)
        if result:
            return { "result" : True, "rc" : 0, "latest_commit" : result }
        return { "result" : False, "rc" : 255, "msg" : "Unexpected result from API call" }
    
