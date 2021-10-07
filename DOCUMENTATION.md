# pyhypixel documentation

1. [HypixelAPI methods](#hypixelapi-methods)
2. [Player methods](#player-methods)
3. [Guild methods](#guild-methods)
4. [GameTypes](#gametypes)

---

## HypixelAPI methods

This class contains general api methods.

Get an instance by using:

```python
api = hypixelapi.HypixelAPI('YOUR_HYPIXEL_API_KEY')
```

Once you have your instance you can use the following methods:

### api.get_api_key()

Returns a dictionary with all the informations regarding the api key in use.

### api.get_player(player)

Args:

- **player**: string username or uuid

Returns a [Player](#player-methods) instance with the given username or uuid.

### api.get_guid_by_id(guild_id)

Args:

- **guild_id**: string guild id

Returns a [Guild](#guild-methods) instance with the given id.

### api.get_guid_by_name(guild_name)

Args:

- **guild_name**: string guild name

Returns a [Guild](#guild-methods) instance with the given name.

### api.get_leaderboards(game_type)

Args:

- **game_type**: default is `None` and returns leaderboards for all the game modes. Accepts a [GameType](#gametypes) enum and returns leaderboards only for the specified GameType. You can access GameTypes by using `hypixelapi.GameType.GAME_NAME` where _GAME_NAME_ is one of [this list](#gametypes).
  
Returns a dictionary containing the leaderboards (check the argument for details).

### api.get_boosters()

Returns a dictionary containing all hypixel boosters.

### api.get_player_count()

Returns current player count in the entire Hypixel network.

### api.get_game_counts(game_type)

Args:

- **game_type**: default is `None` and returns game count for all the game modes. Accepts a [GameType](#gametypes) enum and returns game count only for the specified GameType. You can access GameTypes by using `hypixelapi.GameType.GAME_NAME` where _GAME_NAME_ is one of [this list](#gametypes).

Returns a dictionary containing the game count (check the argument for details).

### api.get_watchdog_stats()

Returns a dictionary containing statistics about Watchdog and Staff bans.

### api.get_skyblock_auctions(page)

Args:

- **page**: int, default is 0

Returns a dictionary containing Skyblock auctions (max 1000 results per page). If the page is not found, `Page not found` is returned.

### api.get_skyblock_bazaar()

Returns a dictionary containing all bazaar items and their sell summary, buy summary and quick status.

### api.get_skyblock_news()

Returns a dictionary containing skyblock news with a title, description and thread.

---

## Player methods

This class contains player related methods.

Get an instance by using one of the two following methods:

```python
# first method using username
player_by_username = api.get_player('SonoMichele')

# second method using uuid
player_by_username = api.get_player('e6c63b4bccc8465189d0b60fb6d56cc4')
```

Once you have your instance you can use the following methods:

### player.get_friends()

Returns a dictionary containing a list of friends.

### player.get_status()

Returns a dictionary containing the current status of a player (online and where, or offline).

### player.get_recent_games()

Returns a dictionary containing max 100 recent games (games are stored for max 3 days).

### player.get_skyblock_auctions()

Returns a dictionary containing all the Skyblock auctions of the current player.

### player.get_skyblock_profiles()

Returns a dictionary containing all the Skyblock profiles of the current player.

### player.get_guild()

Returns the [Guild](#guild-methods) of the current player (None if the player isn't in a guild).

### player.get_name()

Returns the player display name.
New in version 1.1.0

### player.get_achievements()

Returns a dictionary containing the player achievements.
New in version 1.1.0

### player.get_stats(game_type)

Args:

- **game_type**: default is `None` and returns stats for all the game modes. Accepts a [GameType](#gametypes) enum and returns stats only for the specified GameType. You can access GameTypes by using `hypixelapi.GameType.GAME_NAME` where _GAME_NAME_ is one of [this list](#gametypes).
  
Returns a dictionary containing the player stats (check the argument for details).
New in version 1.1.0

### player.get_exp()

Returns the player exp.
New in version 1.1.0

### player.get_bedwars_exp()

Returns the players bedwars exp.

### player.get_level()

Returns the player current level.
New in version 1.1.0

### player.get_raw_player()

Returns a raw json containing all the information about the player.
New in version 1.1.0

### player.get_rank()

Returns the player rank. Returns None if player hasn't rank.
New in version 1.2.0

### player.get_karma()

Returns the player karma.
New in version 1.2.0

### player.get_mc_version()

Returns the last version the player logged in to the sever.
New in version 1.2.0

---

## Guild methods

This class contains guild related methods.

Get an instance by using one of the three following methods:

```python
# first method using guild id
guild_by_id = api.get_guild_by_id('52e57a1c0cf2e250d1cd00f8')

# second method using guild name
guild_by_name = api.get_guild_by_name('The Sloths')

# third method using a player instance
guild_by_player = player.get_guild()
```

Once you have your instance you can use the following methods:

### guild.get_id()

Returns the id of the current guild.

### guild.get_name()

Returns the name of the current guild.

### guild.get_description()

Returns the description of the current guild (None if it hasn't a description).

### guild.get_tag()

Returns the tag of the current guild (None if it hasn't a tag).

### guild.get_members()

Returns a dictionary containing the list of guild members.

### guild.get_achievements()

Returns a dictionary containing the list of achievements the guild has completed.

### guild.get_ranks()

Returns a dictionary containing the list of guild's ranks.

### guild.get_raw_guild()

Returns a raw json with all the informations about the guild ([example](https://github.com/HypixelDev/PublicAPI/blob/master/Documentation/methods/guild.md))

### guild.get_exp()

Returns the guild exp.
New in version 1.1.0

### guild.get_created()

Returns date when the guild was created as an epoch time format.
New in version 1.2.0
---

## GameTypes

You can access those by using `hypixelapi.GameType.GAME_NAME` where _GAME_NAME_ is one of the list below.

All the available GAME TYPES on Hypixel Network:

- QUAKECRAFT
- WALLS
- PAINTBALL
- SURVIVAL_GAMES
- TNTGAMES
- VAMPIREZ
- WALLS3
- ARCADE
- ARENA
- MCGO
- UHC
- BATTLEGROUND
- SUPER_SMASH
- GINGERBREAD
- HOUSING
- SKYWARS
- TRUE_COMBAT
- SPEED_UHC
- SKYCLASH
- LEGACY
- PROTOTYPE
- BEDWARS
- MURDER_MYSTERY
- BUILD_BATTLE
- DUELS
- SKYBLOCK
- PIT

---

[GO UP](#pyhypixel-documentation)
