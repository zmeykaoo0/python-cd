from aiogram.types import Message
from aiogram import Dispatcher, Bot, executor
from aiogram.dispatcher.filters import Text

telegram_bot = Bot('6285007822:AAFPtrlyywe4q9x4yMp6GA-aDzDsbvMT-VA')
dispatcher = Dispatcher(telegram_bot)
bot = telegram_bot

@dispatcher.message_handler(text='бот')
async def cmd_start(message: Message) -> None:
  await message.answer("я здесь господин")

@dispatcher.message_handler(text='команды')
async def cmd_start(message: Message) -> None:
  await message.answer(" пнуть, ударить ,дать пять ,записать на ноготочки ,испугать , убить , купить , продать , нанять ,подстричь,извиниться,прижать,пожать руку,расстрелять, дальше лень было ")

@dispatcher.message_handler(Text(equals="пнуть",ignore_case=True))
async def print_message(message: Message) -> None:

  if message.reply_to_message and message.text.lower()=='пнуть':
    user1 = message.from_user
    user2 = message.reply_to_message.from_user

  await message.answer(
    f'<a href="t.me/{user1.username}">{user1.full_name}</a> пнул <a href="t.me/{user2.username}">{user2.full_name}</a>',
    parse_mode='html',disable_web_page_preview=True
  )

  @dispatcher.message_handler(Text(equals="ударить", ignore_case=True))
  async def print_message(message: Message) -> None:

    if message.reply_to_message and message.text.lower() == 'ударить':
      user1 = message.from_user
      user2 = message.reply_to_message.from_user
    await message.answer(
      f'<a href="t.me/{user1.username}">{user1.full_name}</a> ударил <a href="t.me/{user2.username}">{user2.full_name}</a>',
      parse_mode='html', disable_web_page_preview=True
    )

  @dispatcher.message_handler(Text(equals="дать пять", ignore_case=True))
  async def print_message(message: Message) -> None:

    if message.reply_to_message and message.text.lower() == 'дать пять':
      user1 = message.from_user
      user2 = message.reply_to_message.from_user
    await message.answer(
      f'<a href="t.me/{user1.username}">{user1.full_name}</a> дал пять <a href="t.me/{user2.username}">{user2.full_name}</a>',
      parse_mode='html', disable_web_page_preview=True
    )

  @dispatcher.message_handler(Text(equals="записать на нагаточки", ignore_case=True))
  async def print_message(message: Message) -> None:

    if message.reply_to_message and message.text.lower() == 'записать на нагаточки':
      user1 = message.from_user
      user2 = message.reply_to_message.from_user
    await message.answer(
      f'<a href="t.me/{user1.username}">{user1.full_name}</a> записал на нагаточки <a href="t.me/{user2.username}">{user2.full_name}</a>',
      parse_mode='html', disable_web_page_preview=True
    )

  @dispatcher.message_handler(Text(equals="испугать", ignore_case=True))
  async def print_message(message: Message) -> None:

    if message.reply_to_message and message.text.lower() == 'испугать':
      user1 = message.from_user
      user2 = message.reply_to_message.from_user
    await message.answer(
      f'<a href="t.me/{user1.username}">{user1.full_name}</a> напугал <a href="t.me/{user2.username}">{user2.full_name}</a>',
      parse_mode='html', disable_web_page_preview=True
    )
  @dispatcher.message_handler(Text(equals="убить", ignore_case=True))
  async def print_message(message: Message) -> None:

    if message.reply_to_message and message.text.lower() == 'убить':
      user1 = message.from_user
      user2 = message.reply_to_message.from_user
    await message.answer(
      f'<a href="t.me/{user1.username}">{user1.full_name}</a> убил <a href="t.me/{user2.username}">{user2.full_name}</a>',
      parse_mode='html', disable_web_page_preview=True
    )

    @dispatcher.message_handler(Text(equals="купить", ignore_case=True))
    async def print_message(message: Message) -> None:

      if message.reply_to_message and message.text.lower() == 'купить':
        user1 = message.from_user
        user2 = message.reply_to_message.from_user
      await message.answer(
        f'<a href="t.me/{user1.username}">{user1.full_name}</a> купил <a href="t.me/{user2.username}">{user2.full_name}</a>',
        parse_mode='html', disable_web_page_preview=True
      )

      @dispatcher.message_handler(Text(equals="продать", ignore_case=True))
      async def print_message(message: Message) -> None:

        if message.reply_to_message and message.text.lower() == 'продать':
          user1 = message.from_user
          user2 = message.reply_to_message.from_user
        await message.answer(
          f'<a href="t.me/{user1.username}">{user1.full_name}</a> продал <a href="t.me/{user2.username}">{user2.full_name}</a>',
          parse_mode='html', disable_web_page_preview=True
        )

        @dispatcher.message_handler(Text(equals="нанять", ignore_case=True))
        async def print_message(message: Message) -> None:

          if message.reply_to_message and message.text.lower() == 'нанять':
            user1 = message.from_user
            user2 = message.reply_to_message.from_user
          await message.answer(
            f'<a href="t.me/{user1.username}">{user1.full_name}</a> нанял <a href="t.me/{user2.username}">{user2.full_name}</a>',
            parse_mode='html', disable_web_page_preview=True
          )

          @dispatcher.message_handler(Text(equals="подстричь", ignore_case=True))
          async def print_message(message: Message) -> None:

            if message.reply_to_message and message.text.lower() == 'подстричь':
              user1 = message.from_user
              user2 = message.reply_to_message.from_user
            await message.answer(
              f'<a href="t.me/{user1.username}">{user1.full_name}</a> подстриг <a href="t.me/{user2.username}">{user2.full_name}</a>',
              parse_mode='html', disable_web_page_preview=True
            )

            @dispatcher.message_handler(Text(equals="извиниться", ignore_case=True))
            async def print_message(message: Message) -> None:

              if message.reply_to_message and message.text.lower() == 'извиниться':
                user1 = message.from_user
                user2 = message.reply_to_message.from_user
              await message.answer(
                f'<a href="t.me/{user1.username}">{user1.full_name}</a> извинился <a href="t.me/{user2.username}">{user2.full_name}</a>',
                parse_mode='html', disable_web_page_preview=True
              )
  @dispatcher.message_handler(Text(equals="прижать", ignore_case=True))
  async def print_message(message: Message) -> None:

    if message.reply_to_message and message.text.lower() == 'прижать':
      user1 = message.from_user
      user2 = message.reply_to_message.from_user
    await message.answer(
      f'<a href="t.me/{user1.username}">{user1.full_name}</a> прижал <a href="t.me/{user2.username}">{user2.full_name}</a>',
      parse_mode='html', disable_web_page_preview=True
    )
  @dispatcher.message_handler(Text(equals="пожать руку", ignore_case=True))
  async def print_message(message: Message) -> None:

    if message.reply_to_message and message.text.lower() == 'пожать руку':
      user1 = message.from_user
      user2 = message.reply_to_message.from_user
    await message.answer(
      f'<a href="t.me/{user1.username}">{user1.full_name}</a> пожал руку <a href="t.me/{user2.username}">{user2.full_name}</a>',
      parse_mode='html', disable_web_page_preview=True
    )
    @dispatcher.message_handler(Text(equals="расстрелять", ignore_case=True))
    async def print_message(message: Message) -> None:

      if message.reply_to_message and message.text.lower() == 'расстрелять':
        user1 = message.from_user
        user2 = message.reply_to_message.from_user
      await message.answer(
        f'<a href="t.me/{user1.username}">{user1.full_name}</a> расстрелил <a href="t.me/{user2.username}">{user2.full_name}</a>',
        parse_mode='html', disable_web_page_preview=True
      )

      @dispatcher.message_handler(Text(equals="уничтожить", ignore_case=True))
      async def print_message(message: Message) -> None:

        if message.reply_to_message and message.text.lower() == 'уничтожить':
          user1 = message.from_user
          user2 = message.reply_to_message.from_user
        await message.answer(
          f'<a href="t.me/{user1.username}">{user1.full_name}</a> уничтожил <a href="t.me/{user2.username}">{user2.full_name}</a>',
          parse_mode='html', disable_web_page_preview=True
        )

        @dispatcher.message_handler(Text(equals="щекотать", ignore_case=True))
        async def print_message(message: Message) -> None:

          if message.reply_to_message and message.text.lower() == 'щекотать':
            user1 = message.from_user
            user2 = message.reply_to_message.from_user
          await message.answer(
            f'<a href="t.me/{user1.username}">{user1.full_name}</a> защекотал <a href="t.me/{user2.username}">{user2.full_name}</a>',
            parse_mode='html', disable_web_page_preview=True
          )

          @dispatcher.message_handler(Text(equals="обнять", ignore_case=True))
          async def print_message(message: Message) -> None:

            if message.reply_to_message and message.text.lower() == 'обнять':
              user1 = message.from_user
              user2 = message.reply_to_message.from_user
            await message.answer(
              f'<a href="t.me/{user1.username}">{user1.full_name}</a> обнял <a href="t.me/{user2.username}">{user2.full_name}</a>',
              parse_mode='html', disable_web_page_preview=True
            )

            @dispatcher.message_handler(Text(equals="похвалить", ignore_case=True))
            async def print_message(message: Message) -> None:

              if message.reply_to_message and message.text.lower() == 'похвалить':
                user1 = message.from_user
                user2 = message.reply_to_message.from_user
              await message.answer(
                f'<a href="t.me/{user1.username}">{user1.full_name}</a> похвалил <a href="t.me/{user2.username}">{user2.full_name}</a>',
                parse_mode='html', disable_web_page_preview=True
              )

              @dispatcher.message_handler(Text(equals="сжечь", ignore_case=True))
              async def print_message(message: Message) -> None:

                if message.reply_to_message and message.text.lower() == 'сжечь':
                  user1 = message.from_user
                  user2 = message.reply_to_message.from_user
                await message.answer(
                  f'<a href="t.me/{user1.username}">{user1.full_name}</a> сжег <a href="t.me/{user2.username}">{user2.full_name}</a>',
                  parse_mode='html', disable_web_page_preview=True
                )

                @dispatcher.message_handler(Text(equals="пригласить на чай", ignore_case=True))
                async def print_message(message: Message) -> None:

                  if message.reply_to_message and message.text.lower() == 'пригласить на чай':
                    user1 = message.from_user
                    user2 = message.reply_to_message.from_user
                  await message.answer(
                    f'<a href="t.me/{user1.username}">{user1.full_name}</a> пригласил на чай <a href="t.me/{user2.username}">{user2.full_name}</a>',
                    parse_mode='html', disable_web_page_preview=True
                  )

                  @dispatcher.message_handler(Text(equals="покормить", ignore_case=True))
                  async def print_message(message: Message) -> None:

                    if message.reply_to_message and message.text.lower() == 'покормить':
                      user1 = message.from_user
                      user2 = message.reply_to_message.from_user
                    await message.answer(
                      f'<a href="t.me/{user1.username}">{user1.full_name}</a> покормил <a href="t.me/{user2.username}">{user2.full_name}</a>',
                      parse_mode='html', disable_web_page_preview=True
                    )

                    @dispatcher.message_handler(Text(equals="сфоткать", ignore_case=True))
                    async def print_message(message: Message) -> None:

                      if message.reply_to_message and message.text.lower() == 'сфоткать':
                        user1 = message.from_user
                        user2 = message.reply_to_message.from_user
                      await message.answer(
                        f'<a href="t.me/{user1.username}">{user1.full_name}</a> сфоткал <a href="t.me/{user2.username}">{user2.full_name}</a>',
                        parse_mode='html', disable_web_page_preview=True
                      )

                      @dispatcher.message_handler(Text(equals="расчленить", ignore_case=True))
                      async def print_message(message: Message) -> None:

                        if message.reply_to_message and message.text.lower() == 'расчленить':
                          user1 = message.from_user
                          user2 = message.reply_to_message.from_user
                        await message.answer(
                          f'<a href="t.me/{user1.username}">{user1.full_name}</a> расчленил <a href="t.me/{user2.username}">{user2.full_name}</a>',
                          parse_mode='html', disable_web_page_preview=True
                        )

                        @dispatcher.message_handler(Text(equals="вскрыть вены", ignore_case=True))
                        async def print_message(message: Message) -> None:

                          if message.reply_to_message and message.text.lower() == 'вскрыть вены':
                            user1 = message.from_user
                            user2 = message.reply_to_message.from_user
                          await message.answer(
                            f'<a href="t.me/{user1.username}">{user1.full_name}</a> вскрыл вены <a href="t.me/{user2.username}">{user2.full_name}</a>',
                            parse_mode='html', disable_web_page_preview=True
                          )

                          @dispatcher.message_handler(Text(equals="удачно поговорить", ignore_case=True))
                          async def print_message(message: Message) -> None:

                            if message.reply_to_message and message.text.lower() == 'удачно поговорить':
                              user1 = message.from_user
                              user2 = message.reply_to_message.from_user
                            await message.answer(
                              f'<a href="t.me/{user1.username}">{user1.full_name}</a> удачно поговорил <a href="t.me/{user2.username}">{user2.full_name}</a>',
                              parse_mode='html', disable_web_page_preview=True
                            )

                            @dispatcher.message_handler(Text(equals="раздеть", ignore_case=True))
                            async def print_message(message: Message) -> None:

                              if message.reply_to_message and message.text.lower() == 'раздеть':
                                user1 = message.from_user
                                user2 = message.reply_to_message.from_user
                              await message.answer(
                                f'<a href="t.me/{user1.username}">{user1.full_name}</a> раздел <a href="t.me/{user2.username}">{user2.full_name}</a>',
                                parse_mode='html', disable_web_page_preview=True
                              )

                              @dispatcher.message_handler(Text(equals="отправить холоднй стикер", ignore_case=True))
                              async def print_message(message: Message) -> None:

                                if message.reply_to_message and message.text.lower() == 'отправить холоднй стикер':
                                  user1 = message.from_user
                                  user2 = message.reply_to_message.from_user
                                await message.answer(
                                  f'<a href="t.me/{user1.username}">{user1.full_name}</a> отправил холодный стикер <a href="t.me/{user2.username}">{user2.full_name}</a>',
                                  parse_mode='html', disable_web_page_preview=True
                                )

                                @dispatcher.message_handler(Text(equals="нанять в собеседники", ignore_case=True))
                                async def print_message(message: Message) -> None:

                                  if message.reply_to_message and message.text.lower() == 'нанять в собеседники':
                                    user1 = message.from_user
                                    user2 = message.reply_to_message.from_user
                                  await message.answer(
                                    f'<a href="t.me/{user1.username}">{user1.full_name}</a> нанял в собеседники <a href="t.me/{user2.username}">{user2.full_name}</a>',
                                    parse_mode='html', disable_web_page_preview=True
                                  )

                                  @dispatcher.message_handler(Text(equals="окозаться сзади", ignore_case=True))
                                  async def print_message(message: Message) -> None:

                                    if message.reply_to_message and message.text.lower() == 'окозаться сзади':
                                      user1 = message.from_user
                                      user2 = message.reply_to_message.from_user
                                    await message.answer(
                                      f'<a href="t.me/{user1.username}">{user1.full_name}</a> окозался сзади <a href="t.me/{user2.username}">{user2.full_name}</a>',
                                      parse_mode='html', disable_web_page_preview=True
                                    )

                                    @dispatcher.message_handler(Text(equals="отрубить голову", ignore_case=True))
                                    async def print_message(message: Message) -> None:

                                      if message.reply_to_message and message.text.lower() == 'отрубить голову':
                                        user1 = message.from_user
                                        user2 = message.reply_to_message.from_user
                                      await message.answer(
                                        f'<a href="t.me/{user1.username}">{user1.full_name}</a> отрубил голову <a href="t.me/{user2.username}">{user2.full_name}</a>',
                                        parse_mode='html', disable_web_page_preview=True
                                      )

                                      @dispatcher.message_handler(Text(equals="сделать шашлык", ignore_case=True))
                                      async def print_message(message: Message) -> None:

                                        if message.reply_to_message and message.text.lower() == 'сделать шашлык':
                                          user1 = message.from_user
                                          user2 = message.reply_to_message.from_user
                                        await message.answer(
                                          f'<a href="t.me/{user1.username}">{user1.full_name}</a> сделал шашлик <a href="t.me/{user2.username}">{user2.full_name}</a>',
                                          parse_mode='html', disable_web_page_preview=True
                                        )

                                        @dispatcher.message_handler(Text(equals="предать", ignore_case=True))
                                        async def print_message(message: Message) -> None:

                                          if message.reply_to_message and message.text.lower() == 'предать':
                                            user1 = message.from_user
                                            user2 = message.reply_to_message.from_user
                                          await message.answer(
                                            f'<a href="t.me/{user1.username}">{user1.full_name}</a> предал <a href="t.me/{user2.username}">{user2.full_name}</a>',
                                            parse_mode='html', disable_web_page_preview=True
                                          )

                                          @dispatcher.message_handler(Text(equals="поцеловать", ignore_case=True))
                                          async def print_message(message: Message) -> None:

                                            if message.reply_to_message and message.text.lower() == 'поцеловать':
                                              user1 = message.from_user
                                              user2 = message.reply_to_message.from_user
                                            await message.answer(
                                              f'<a href="t.me/{user1.username}">{user1.full_name}</a> поцеловал <a href="t.me/{user2.username}">{user2.full_name}</a>',
                                              parse_mode='html', disable_web_page_preview=True
                                            )

                                            @dispatcher.message_handler(
                                              Text(equals="украсть", ignore_case=True))
                                            async def print_message(message: Message) -> None:

                                              if message.reply_to_message and message.text.lower() == 'украсть':
                                                user1 = message.from_user
                                                user2 = message.reply_to_message.from_user
                                              await message.answer(
                                                f'<a href="t.me/{user1.username}">{user1.full_name}</a> украл <a href="t.me/{user2.username}">{user2.full_name}</a>',
                                                parse_mode='html', disable_web_page_preview=True
                                              )

