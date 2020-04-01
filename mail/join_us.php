<?php
// Check for empty fields
if(empty($_POST['name'])        ||
   empty($_POST['date'])        ||
   empty($_POST['institution']) ||
   empty($_POST['country'])     ||
   empty($_POST['agreement']))
   {
   echo "No arguments Provided!";
   return false;
   }
   
$name = strip_tags(htmlspecialchars($_POST['name']));
$date = strip_tags(htmlspecialchars($_POST['date']));
$institution = strip_tags(htmlspecialchars($_POST['institution']));
$country = strip_tags(htmlspecialchars($_POST['country']));
$agreement = strip_tags(htmlspecialchars($_POST['agreement']));
   
// Create the email and send the message
$to = 'contact.GCCR@gmail.com'; // Add your email address inbetween the '' replacing yourname@yourdomain.com - This is where the form will send a message to.
$email_subject = "Joining GCCR (from website):  $name";
$email_body = "You have received a new membership request from your website contact form.\n\n"."Here are the details:\n\nName: $name\n\nDate: $date\n\nInstitution: $institution\n\nCountry: $country\n\nAgreement to become a GCCR member: $agreement";
$headers = "From: contact.GCCR@gmail.com\n"; // This is the email address the generated message will be from. We recommend using something like noreply@yourdomain.com.
$headers .= "Reply-To: $email_address";   
mail($to,$email_subject,$email_body,$headers);
return true;         
?>