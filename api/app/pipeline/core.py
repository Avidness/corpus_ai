from app.agents.BigPictureArchitectAgent import BigPictureArchitectAgent

async def pipeline_core(user_input: str):
  yield "Beginning request..."

  try:
      agent = BigPictureArchitectAgent(user_input)
      outline = await agent.generate_outline()
      
      for chap in outline.chapters:
        yield chap.to_json()

      for char in outline.characters:
        yield char.to_json()
    
  except Exception as e:
      yield f"Error running core pipeline: {e}"

  #async for result in await agent.generate_outline():
  #  yield result