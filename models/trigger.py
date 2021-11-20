from plugins.github.includes import github

import jimi

class _githubTriggerLatestCommitPoll(jimi.trigger._trigger):
    schedule = "300-900s"
    owner = str()
    repo = str()
    lastestCommit = str()

    def doCheck(self):
        try:
            latestCommit = self.lastestCommit
        except:
            latestCommit = ""

        events = []
        githubObj = github._github()
        result = githubObj.getLatestCommit(self.owner,self.repo)
        if result:
            if result["sha"] != latestCommit:
                events.append(result)
                self.lastestCommit = result["sha"]
                self.update(["lastestCommit"])

        self.result = { "events" : events, "var" : {}, "plugin" : {} }
        return self.result["events"]