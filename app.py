import asyncio  
import sys 
from flask import Flask, request, Response  
from botbuilder.core import (  
    BotFrameworkAdapter,  
    BotFrameworkAdapterSettings,     
    TurnContext,      
)  
rom botbuilder.schema import Activity  
from echobot import*  
bot = EchoBot()  
SETTINGS = BotFrameworkAdapterSettings("299f6045-9b9a-48bd-a154-71626fdb0983","2a3547aa-4ef8-4817-9002-bec028f93c5e")  
ADAPTER = BotFrameworkAdapter(SETTINGS)  
LOOP = asyncio.get_event_loop()  
@app.route("/api/messages", methods=["POST"])  
def messages():  
    if "application/json" in request.headers["Content-Type"]:  
        body = request.json  
    else:  
        return Response(status=415)  
  
    activity = Activity().deserialize(body)  
    auth_header = (request.headers["Authorization"] if "Authorization" in request.headers else "")  
  
    async def aux_func(turn_context):  
        await bot.on_turn(turn_context)  
  
    try:  
        task = LOOP.create_task(  
            ADAPTER.process_activity(activity, auth_header, aux_func)  
        )  
        LOOP.run_until_complete(task)  
       
    
    if __name__ == '__main__':  
        app.run(localhOST,3978)  
