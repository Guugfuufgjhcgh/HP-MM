from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class FreeFirePlayer(Resource):
    def get(self):
        data = [
            {
                "id": "12345678",
                "cached": True,
                "message": {
                    "account": {
                        "badge": "17",
                        "bannerId": "901040014",
                        "brPoint": "4370",
                        "createdAt": "1512595169",
                        "csPoint": "64",
                        "exp": "1925563",
                        "hasElitePass": True,
                        "headPic": 902000154,
                        "lastLogin": "1718213301",
                        "level": "66",
                        "likes": "3383012",
                        "nickname": "FB:ㅤ@GMRemyX",
                        "profile": {},
                        "server": "SG",
                        "uid": "12345678"
                    },
                    "guild": {
                        "guildCapacity": "50",
                        "guildLevel": "6",
                        "id": "60893361",
                        "leaderUID": "12345678",
                        "name": "MᴜᴍᴍʏEᴠᴀTᴇᴀᴍ",
                        "numberOfMembers": "43"
                    },
                    "guildLeader": {
                        "badge": "17",
                        "brPoint": "4370",
                        "createdAt": "1512595169",
                        "csPoint": "64",
                        "exp": "1925563",
                        "hasElitePass": True,
                        "lastLogin": "1718213301",
                        "level": "66",
                        "likes": "3383012",
                        "nickname": "FB:ㅤ@GMRemyX",
                        "profile": {},
                        "server": "SG",
                        "uid": "12345678"
                    },
                    "socialStyle": {
                        "bio": "FB & YT GM Remy | TikTok :gmremyx | IG GM Remy"
                    }
                }
            },
            {
                "id": "87654321",
                "cached": False,
                "message": {
                    "basicInfo": {
                        "accountId": "12345678",
                        "accountPrefers": {},
                        "accountType": 1,
                        "badgeCnt": 17,
                        "badgeId": 1001000073,
                        "bannerId": 901040014,
                        "createAt": "1512595169",
                        "csMaxRank": 216,
                        "csRank": 216,
                        "csRankingPoints": 64,
                        "exp": 1925563,
                        "externalIconInfo": {
                            "showType": "ExternalIconShowType_FRIEND",
                            "status": "ExternalIconStatus_NOT_IN_USE"
                        },
                        "hasElitePass": True,
                        "headPic": 902000154,
                        "lastLoginAt": "1718213301",
                        "level": 66,
                        "liked": 3383012,
                        "maxRank": 221,
                        "nickname": "FB:ㅤ@GMRemyX",
                        "rank": 221,
                        "rankingPoints": 4370,
                        "region": "SG",
                        "releaseVersion": "OB44",
                        "role": 4,
                        "seasonId": 39,
                        "showBrRank": True,
                        "showCsRank": True,
                        "socialHighLightsWithBasicInfo": {},
                        "title": 904090023,
                        "weaponSkinShows": [907103421, 912042002, 914000002]
                    },
                    "captainBasicInfo": {
                        "accountId": "12345678",
                        "accountPrefers": {},
                        "accountType": 1,
                        "badgeCnt": 17,
                        "badgeId": 1001000073,
                        "bannerId": 901040014,
                        "createAt": "1512595169",
                        "csMaxRank": 216,
                        "csRank": 216,
                        "csRankingPoints": 64,
                        "exp": 1925563,
                        "externalIconInfo": {
                            "showType": "ExternalIconShowType_FRIEND",
                            "status": "ExternalIconStatus_NOT_IN_USE"
                        },
                        "hasElitePass": True,
                        "headPic": 902000154,
                        "lastLoginAt": "1718213301",
                        "level": 66,
                        "liked": 3383012,
                        "maxRank": 221,
                        "nickname": "FB:ㅤ@GMRemyX",
                        "rank": 221,
                        "rankingPoints": 4370,
                        "region": "SG",
                        "releaseVersion": "OB44",
                        "role": 4,
                        "seasonId": 39,
                        "showBrRank": True,
                        "showCsRank": True,
                        "socialHighLightsWithBasicInfo": {},
                        "title": 904090023,
                        "weaponSkinShows": [907103421, 912042002, 914000002]
                    },
                    "clanBasicInfo": {
                        "capacity": 50,
                        "captainId": "12345678",
                        "clanId": "60893361",
                        "clanLevel": 6,
                        "clanName": "MᴜᴍᴍʏEᴠᴀTᴇᴀᴍ",
                        "memberNum": 43
                    },
                    "creditScoreInfo": {
                        "creditScore": 100,
                        "periodicSummaryEndTime": "1717984821",
                        "rewardState": "REWARD_STATE_UNCLAIMED"
                    },
                    "diamondCostRes": {
                        "diamondCost": 390
                    },
                    "equippedAch": [
                        {
                            "achId": 32006,
                            "level": 2
                        },
                        {
                            "achId": 21009,
                            "level": 3
                        },
                        {
                            "achId": 21006,
                            "level": 3
                        },
                        {
                            "achId": 21008,
                            "level": 3
                        }
                    ],
                    "historyEpInfo": [
                        {
                            "badgeCnt": 121,
                            "bpIcon": "UI_BP_Emoji_Videogame",
                            "epBadge": 1001000072,
                            "epEventId": 72,
                            "eventName": "T_44_H_BP72_NAME",
                            "maxLevel": 100,
                            "ownedPass": True
                        },
                        {
                            "badgeCnt": 100,
                            "bpIcon": "UI_BP_Emoji_Pointed",
                            "epBadge": 1001000071,
                            "epEventId": 71,
                            "eventName": "T_43_H_BP71_NAME",
                            "maxLevel": 100,
                            "ownedPass": True
                        },
                        {
                            "badgeCnt": 107,
                            "bpIcon": "UI_BP_Emoji_Frog",
                            "epBadge": 1001000070,
                            "epEventId": 70,
                            "eventName": "T_43_H_BP70_NAME",
                            "maxLevel": 100,
                            "ownedPass": True
                        },
                        {
                            "badgeCnt": 101,
                            "bpIcon": "UI_BP_Emoji_Asura",
                            "epBadge": 1001000069,
                            "epEventId": 69,
                            "eventName": "T_43_H_BP69_NAME",
                            "maxLevel": 100,
                            "ownedPass": True
                        },
                        {
                            "badgeCnt": 163,
                            "bpIcon": "UI_BP_Emoji_Electri",
                            "epBadge": 1001000068,
                            "epEventId": 68,
                            "eventName": "T_42_H_BP68_NAME",
                            "maxLevel": 150,
                            "ownedPass": True
                        },
                        {
                            "badgeCnt": 155,
                            "bpIcon": "UI_BP_Emoji_Watcher",
                            "epBadge": 1001000067,
                            "epEventId": 67,
                            "eventName": "T_42_H_BP67_NAME",
                            "maxLevel": 150,
                            "ownedPass": True
                        },
                        {
                            "badgeCnt": 178,
                            "bpIcon": "UI_BP_Emoji_Puppets",
                            "epBadge": 1001000066,
                            "epEventId": 66,
                            "eventName": "T_41_H_BP66_NAME",
                            "maxLevel": 150,
                            "ownedPass": True
                        },
                        {
                            "badgeCnt": 134,
                            "bpIcon": "UI_BP_Emoji_Poseidon",
                            "epBadge": 1001000065,
                            "epEventId": 65,
                            "eventName": "T_41_H_BP65_NAME",
                            "maxLevel": 150,
                            "ownedPass": True
                        },
                        {
                            "badgeCnt": 97,
                            "bpIcon": "UI_BP_Emoji_Cook",
                            "epBadge": 1001000064,
                            "epEventId": 64,
                            "eventName": "T_40H_BP64_NAME",
                            "maxLevel": 100,
                            "ownedPass": True
                        },
                        {
                            "badgeCnt": 95,
                            "bpIcon": "UI_BP_Emoji_Crusade",
                            "epBadge": 1001000063,
                            "epEventId": 63,
                            "eventName": "T_40_H_BP63_NAME",
                            "maxLevel": 100,
                            "ownedPass": True
                        },
                        {
                            "badgeCnt": 58,
                            "bpIcon": "UI_BP_Emoji_Jin",
                            "epBadge": 1001000062,
                            "epEventId": 62,
                            "eventName": "T_39_H_BP62_NAME",
                            "maxLevel": 60,
                            "ownedPass": True
                        }
                    ],
                    "passInfo": {
                        "chances": 3,
                        "epMax": 150,
                        "level": 13,
                        "rewardTime": "1718000400",
                        "time": "1717927200"
                    },
                    "rewards": {
                        "allChosen": 6,
                        "elitePass": 7,
                        "freePass": 14,
                        "nextPeriods": [
                            {
                                "rewardTime": "1718000400",
                                "startTime": "1717927200"
                            }
                        ],
                        "rewardsReceived": [
                            {
                                "bpIcon": "UI_BP_Emoji_Wounded",
                                "epBadge": 1001000018,
                                "epEventId": 18,
                                "eventName": "T_23_H_BP18_NAME",
                                "maxLevel": 50,
                                "ownedPass": True
                            },
                            {
                                "bpIcon": "UI_BP_Emoji_Crusade",
                                "epBadge": 1001000063,
                                "epEventId": 63,
                                "eventName": "T_40_H_BP63_NAME",
                                "maxLevel": 100,
                                "ownedPass": True
                            },
                            {
                                "bpIcon": "UI_BP_Emoji_Jin",
                                "epBadge": 1001000062,
                                "epEventId": 62,
                                "eventName": "T_39_H_BP62_NAME",
                                "maxLevel": 60,
                                "ownedPass": True
                            }
                        ],
                        "seasonId": 40,
                        "startTime": "1717927200"
                    },
                    "spEndAt": "1779628981",
                    "ticketNum": 0,
                    "totalEarn": 10,
                    "vip": True,
                    "worldR": {
                        "maxLevel": 180,
                        "monsterId": 10110014,
                        "maxLevelN": 13,
                        "level": 15,
                        "id": 10120001,
                        "count": 200
                    },
                    "friendInfo": [
                        {
                            "id": "9074146109",
                            "nickname": "@HP LVL BYTE⁴⁴⁴모",
                            "server": "EN",
                            "level": 37,
                            "likes": 4026,
                            "guild": {
                                "name": "HP LVL BYTE Guild",
                                "level": 100,
                                "exp": 1000,
                                "leader": {
                                    "nickname": "HP LVL BYTE",
                                    "server": "EN"
                                }
                            },
                            "lastLogin": "2024-06-20 10:51:16"
                        },
                        {
                            "id": "12345678",
                            "nickname": "FB:ㅤ@GMRemyX",
                            "server": "SG",
                            "level": 66,
                            "likes": 3383012,
                            "guild": {
                                "name": "MᴜᴍᴍʏEᴠᴀTᴇᴀᴍ",
                                "level": 6,
                                "leader": {
                                    "nickname": "FB:ㅤ@GMRemyX",
                                    "server": "SG"
                                }
                            },
                            "lastLogin": "1718213301"
                        }
                    ]
                }
            }
        ]

        return jsonify(data)

api.add_resource(FreeFirePlayer, '/api/HPLVL')

if __name__ == '__main__':
    app.run(debug=True)