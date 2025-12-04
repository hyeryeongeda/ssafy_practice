from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

# 의사와 환자간의 M:N관계를 Revervation 모델을 통해서 관리
# : through='Reservation'
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserver_at = models.DateTimeField(auto_now_add=True)

'''
doctor1 = Doctor.objects.create(name = 'alice')
patient1 = Patient.objects.create(name = 'carol')
patient2 = Patient.objects.create(name = 'duke')

# 1.  Reservation 모델을 직접 생성하여 의사와 환자 간의 예약
# alice가 carol을 두통(headache)로 예약
reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
reservation1.save()

# 2. Patient 객체의 doctors 필드(ManyToManyField)를 통해 예약
# duke가 alice로 감기(flue)로 예약
patient2.doctors.add(doctor1, through_defaults={'symptom' : 'flu'})


# 3. Doctor 객체에서 patient_set을 통해 예약을 취소
# carol과 한 예약 취소
doctor1.patient_set.remove(patient1)
'''