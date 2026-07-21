student=input("Are you a student? (yes/no): ")
pets=input("Do you have any pets? (yes/no): ")
smokes=input("Do you smoke? (yes/no): ")

is_student=student=="yes"
has_pets=pets=="yes"
smokes=smokes=="yes"

student_can_rent=is_student and not smokes and not has_pets
non_student_can_rent=not is_student and not smokes and not has_pets
can_rent=student_can_rent or non_student_can_rent

print("can rent:" + str(can_rent))

