from .database import Base
from sqlalchemy import Column, Integer, String, Numeric


class sample_activity(Base):
	__tablename__ = "sample_activity"

	Index = Column(Integer, primary_key=True, index=True)
	EMAIL = Column(String(24), unique=False)
	activity_average_met = Column(Numeric, unique=False)
	activity_cal_active = Column(Integer, unique=False)
	activity_cal_total = Column(Integer, unique=False)
	activity_class_5min = Column(String(4), unique=False)
	activity_daily_movement = Column(Integer, unique=False)
	activity_day_end = Column(String(37), unique=False)
	activity_day_start = Column(String(37), unique=False)
	activity_high = Column(Integer, unique=False)
	activity_inactive = Column(Integer, unique=False)
	activity_inactivity_alerts = Column(Integer, unique=False)
	activity_low = Column(Integer, unique=False)
	activity_medium = Column(Integer, unique=False)
	activity_met_1min = Column(String(4), unique=False)
	activity_met_min_high = Column(Integer, unique=False)
	activity_met_min_inactive = Column(Integer, unique=False)
	activity_met_min_low = Column(Integer, unique=False)
	activity_met_min_medium = Column(Integer, unique=False)
	activity_non_wear = Column(Integer, unique=False)
	activity_rest = Column(Integer, unique=False)
	activity_score = Column(Integer, unique=False)
	activity_score_meet_daily_targets = Column(Integer, unique=False)
	activity_score_move_every_hour = Column(Integer, unique=False)
	activity_score_recovery_time = Column(Integer, unique=False)
	activity_score_stay_active = Column(Integer, unique=False)
	activity_score_training_frequency = Column(Integer, unique=False)
	activity_score_training_volume = Column(Integer, unique=False)
	activity_steps = Column(Integer, unique=False)
	activity_total = Column(Integer, unique=False)
	CONVERT_activity_class_5min = Column(String(864), unique=False)
	CONVERT_activity_met_1min = Column(String(8427), unique=False)
