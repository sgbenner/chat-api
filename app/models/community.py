# class Community(Base):
#     __tablename__ = "community"
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String, index=True)
#     creator_user_id = Column(Integer, ForeignKey("users.id"))
#     settings = Column(types.JSON)
#
#     creator = relationship("User", back_populates="created_communities")
