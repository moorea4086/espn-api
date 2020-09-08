from espn_api.football import League

swid = '{AF6D609F-EBCE-4755-BD7A-C6B8BB2BDB0A}'
espn_s2 = 'AECDi2XzUuQv5Q%2BthjeANwInbcavLa0Zyk5rE2pUX9bQdQubtLOt8FwcfPnpj2%2BxJnZniexSf5SqiawdV6wJy3Nn8Gqhx1XyKWqGW0%2FboFAYPZHgGZDraFDDIT77IwZE9Ok5Ywq%2FfmetLTZ6zraekXO3hfdLWIKOmjTooURlaRPOT%2BoUiorht2I0p%2FReVFVamte36fjvBuOBjDx06nfWN8Lw0VlyJgw9NjNFZGvw4mzRtm6WEolRtp%2F3NXCwa0XZR2KO7WHclu5xx%2BHN7%2FVk1JTCTyb9bnpH2Z0ds8BSEDWAxA%3D%3D'

league = League(league_id=452867, year=2020, espn_s2 = espn_s2, swid = swid)
print(league.teams)
team = league.teams[8]
print(team.roster)
free_agents = league.free_agents(size=5)
print(free_agents)