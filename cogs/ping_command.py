import random

from discord.ext import commands, vbu


class PingCommand(vbu.Cog):

    # A list of strings that get DMd to users to tell them they did a shit job
    # during their day today
    DM_STRINGS = [
        "You're a fucking idiot.",
        "You're a fucking moron.",
        "You should have done better today.",
        "You should have tried harder today.",
        "You should have done more today.",
        "You should have worked harder today.",
        "You should have worked more today.",
        "You should have tried more today.",
        "Nobody wants you around.",
        "You're a fucking loser.",
        "You're a fucking failure.",
        "You're useless.",
        "You're a waste of space.",
        "You're a waste of time.",
        "Nobody likes you.",
        "Everyone hates you and you know it.",
        "You smell like shit.",
        "We deserve better than you.",
        "People wouldn't mind if you went missing.",
        "You're a fucking waste of oxygen.",
        "I hope you cry yourself to sleep at night.",
        "I hope you die in a fire.",
        "I hope you die.",
        "We would be better off without you.",
        "Your birth was a stale joke.",
        "You're not appreciated.",
        "Your \"friends\" talk about you behind your back.",
        "You're not worth the effort.",
        "Your crush doesn't even know you exist.",
        "The voice in your head telling you you're worthless? It's right.",
        "You add nothing of value to this world.",
        "You're a disgrace to humanity.",
        "Your existence is nothing more than a nuisance.",
        "You're a nobody.",
        "You're a pathetic excuse for a human being.",
        "You're a joke.",
        "You're an embarrassment.",
        "Nobody respects you.",
        "You're a disgrace.",
        "Nobody will ever love you.",
        "You're a loser and you know it.",
        "You'll never amount to anything.",
        "You're not worth anyone's time.",
        "Nobody wants to be your friend.",
        "You're a pathetic weakling.",
        "You're a blight on society.",
        "You're a useless parasite.",
        "You're not worth the air you breathe.",
        "Nobody cares about you.",
        "You should have stayed in the womb.",
        "You're an annoying pest.",
        "You're a walking embarrassment.",
        "You're a walking tragedy.",
        "Nobody wants to hear your opinion.",
        "You're a disgrace to your family.",
        "You're an eyesore.",
        "You're a stain on this world.",
        "You're a walking mistake.",
        "You're an embarrassment to be around.",
        "You're an abomination.",
        "You're an insult to intelligence.",
        "You're a walking disaster.",
        "You're nothing but a joke.",
        "Your best days are behind you.",
        "You'll never achieve anything.",
        "You're a complete waste of space.",
        "You make me want to vomit.",
        "You make me cringe.",
        "You're a blight on the world.",
        "You're a walking mistake.",
        "You're an embarrassment to your species.",
        "You're a walking tragedy.",
        "Nobody wants you around.",
        "Nobody likes having you around.",
        "You're a complete nuisance.",
        "You're a complete waste of time.",
        "You're a complete waste of energy.",
        "Your opinion doesn't matter.",
        "You're a complete idiot.",
        "You're not smart enough for this world.",
        "You're a complete embarrassment.",
        "Your presence is a plague upon the world.",
        "You're an insult to the human race.",
        "You're a pathetic excuse for a human being.",
        "You are a walking disaster.",
        "Nobody cares what you think.",
        "Nobody cares what you do.",
        "You're an eyesore.",
        "You're a walking punchline.",
        "You're the reason contraceptives were invented.",
        "https://paypal.me/CalebBartlett",
    ]

    @commands.command(
        application_command_meta=commands.ApplicationCommandMeta(),
    )
    async def depression(self, ctx: vbu.SlashContext):
        """
        Send you a messasge :)
        """

        return await ctx.interaction.response.send_message(
            random.choice(self.DM_STRINGS),
            # ephemeral=True,
        )


def setup(bot: vbu.Bot):
    x = PingCommand(bot)
    bot.add_cog(x)
