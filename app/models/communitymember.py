# class CommunityMember(Base):
#     # can store info in this table about community permissions and settings
#     __tablename__ = "community_member"
#
#     id = Column(String, primary_key=True, index=True)
#     user = Column(Integer, ForeignKey("users.id"))
#     community = Column(Integer, ForeignKey("community.id"))
#
#     communities = relationship("Community", back_populates="users")
