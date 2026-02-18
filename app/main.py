"""
Point d'entrée de l'API Portfolio.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.mongo import connect_mongo, close_mongo
from app.db.neo4j import connect_neo4j, close_neo4j
from app.routers import public, graph, health


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gère le cycle de vie de l'application (startup / shutdown)."""
    # ── Startup ──
    await connect_mongo()
    await connect_neo4j()
    yield
    # ── Shutdown ──
    await close_mongo()
    await close_neo4j()


app = FastAPI(
    title="Portfolio API",
    description="API pour servir les données d'un portfolio personnel (MongoDB + Neo4j)",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS — autorise toutes les origines (à restreindre en prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routers ──────────────────────────────────────
app.include_router(health.router)
app.include_router(public.router)
app.include_router(graph.router)
