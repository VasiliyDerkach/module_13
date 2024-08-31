import asyncio
async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        asyncio.sleep(20//power)
        print(f'Силач {name} поднял {1}' )
    print(f'Силач {name} закончил соревнования.')
async def start_tournament():
    tsk_nik = asyncio.create_task(start_strongman('Nick',8))
    tsk_donl = asyncio.create_task(start_strongman('Donald',9))
    tsk_caml = asyncio.create_task(start_strongman('Camela',6))
    await tsk_nik
    await tsk_donl
    await tsk_caml

asyncio.run(start_tournament())