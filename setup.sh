#!/bin/bash
apt update
apt install -y python3-pip
pip3 install supabase-py
export SUPABASE_URL="your-supabase-url"
export SUPABASE_SERVICE_KEY="your-service-role-key"
python3 bot.py
