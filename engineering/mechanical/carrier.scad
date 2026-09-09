// IDA R1 prototype carrier. Millimetres. Assumed fit; no human-use qualification.
// Retain the OEM insulating case. Measure it before revising these parameters.
case_x=76; case_y=76; clearance=1; rail=5; height=8; lip_h=2; lip=4;
inner_x=case_x+2*clearance; inner_y=case_y+2*clearance;
outer_x=inner_x+2*rail; outer_y=inner_y+2*rail;
module carrier(){
 difference(){
  cube([outer_x,outer_y,height],center=false);
  translate([rail,rail,lip_h]) cube([inner_x,inner_y,height+1]);
  translate([rail+lip,rail+lip,-1]) cube([inner_x-2*lip,inner_y-2*lip,height+2]);
 }
}
module electrode_carrier(contact_d=9){
 difference(){
  cube([24,24,6]);
  translate([12,12,-1]) cylinder(h=8,d=contact_d,$fn=64);
  translate([1,2,2]) cube([3,20,2]);
  translate([20,2,2]) cube([3,20,2]);
 }
}
carrier();
// Uncomment to inspect a separate contact carrier; it has not been rendered here.
// translate([outer_x+10,0,0]) electrode_carrier();
