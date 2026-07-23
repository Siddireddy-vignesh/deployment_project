from fastapi import FastAPI
from supabase import create_client

backend_server_obj = FastAPI() #obj creation

NEXT_PUBLIC_SUPABASE_URL="https://bqkblqyirmwdhozdcndf.supabase.co"
NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY="sb_publishable_x6cEBJpsFyny6cNb7Jc5dg_YO8z9EOS"

supabase_connection_obj = create_client(NEXT_PUBLIC_SUPABASE_URL,NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY)

@backend_server_obj.post("/register")

def register_function(payload:dict):
    #print(payload,"data")
    supabase_connection_obj.table("students").insert(payload).execute()
    return {"msg":"student added successfully"}

