  (
   @register(outgoing=True, pattern=r"^\.fnix$"*)
   async def fnix(e):
     await e.edit(
       "**tu é um corno fnix** \n"
       )